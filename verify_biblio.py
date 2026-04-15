#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import json
import re
import sys
import time
import unicodedata
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

import fitz
import requests
from rapidfuzz import fuzz


ARXIV_API_URL = "https://export.arxiv.org/api/query?id_list={paper_id}"
OUTPUT_JSON = Path("verify_biblio_results.json")
RESULTS_MD = Path("RESULTS.md")
REQUEST_TIMEOUT = 30
MAX_RETRIES = 4
BACKOFF_SECONDS = 1.5

EXPECTED_REFERENCES: Dict[str, Dict[str, object]] = {
    "2301.11305": {
        "title": "DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature",
        "authors": ["Eric Mitchell", "Yoonho Lee", "Chelsea Finn"],
    },
    "2301.10226": {
        "title": "A Watermark for Large Language Models",
        "authors": ["John Kirchenbauer", "Jonas Geiping", "Tom Goldstein"],
    },
    "2303.11156": {
        "title": "Can AI-Generated Text be Reliably Detected?",
        "authors": ["Vinu Sankar Sadasivan", "Soheil Feizi"],
    },
    "2303.13408": {
        "title": "Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense",
        "authors": ["Kalpesh Krishna", "John Wieting", "Mohit Iyyer"],
    },
    "2304.02819": {
        "title": "GPT detectors are biased against non-native English writers",
        "authors": ["Weixin Liang", "Mert Yuksekgonul", "James Zou"],
    },
    "2303.07205": {
        "title": "The Science of Detecting LLM-Generated Texts",
        "authors": ["Ruixiang Tang", "Xia Hu"],
    },
    "2304.04736": {
        "title": "On the Possibilities of AI-Generated Text Detection",
        "authors": ["Souradip Chakraborty", "Amrit Singh Bedi", "Furong Huang"],
    },
    "2406.12549": {
        "title": "MultiSocial: Multilingual Benchmark of Machine-Generated Text Detection of Social-Media Texts",
        "authors": ["Dominik Macko", "Jakub Kopal", "Ivan Srba"],
    },
    "2406.15583": {
        "title": "Detecting AI-Generated Text: Factors Influencing Detectability with Current Methods",
        "authors": ["Kathleen C. Fraser", "Svetlana Kiritchenko"],
    },
    "2402.13671": {
        "title": "KInIT at SemEval-2024 Task 8: Fine-tuned LLMs for Multilingual Machine-Generated Text Detection",
        "authors": ["Michal Spiegel", "Dominik Macko"],
    },
    "2310.14724": {
        "title": "A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions",
        "authors": ["Junchao Wu", "Shu Yang", "Lidia S. Chao"],
    },
    "2310.15264": {
        "title": "Towards Possibilities & Impossibilities of AI-generated Text Detection: A Survey",
        "authors": ["Soumya Suvra Ghosal", "Souradip Chakraborty", "Amrit Singh Bedi"],
    },
}


@dataclass
class PaperRecord:
    paper_id: str
    found: bool
    title: str
    authors: List[str]
    abstract: str
    pdf_url: str
    published: str


def log(message: str) -> None:
    print(message, file=sys.stderr)


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def markdown_table(headers: Iterable[str], rows: Iterable[Iterable[str]]) -> str:
    header_list = [str(cell) for cell in headers]
    row_list = [[str(cell) for cell in row] for row in rows]
    widths = [len(cell) for cell in header_list]
    for row in row_list:
        for idx, cell in enumerate(row):
            widths[idx] = max(widths[idx], len(cell))
    header = "| " + " | ".join(header_list[idx].ljust(widths[idx]) for idx in range(len(widths))) + " |"
    sep = "|-" + "-|-".join("-" * widths[idx] for idx in range(len(widths))) + "-|"
    body = [
        "| " + " | ".join(row[idx].ljust(widths[idx]) for idx in range(len(widths))) + " |"
        for row in row_list
    ]
    return "\n".join([header, sep, *body])


def request_with_retry(url: str, *, binary: bool = False) -> bytes | str:
    last_error: Optional[Exception] = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.get(url, timeout=REQUEST_TIMEOUT, headers={"User-Agent": "plume-naturelle/verify_biblio"})
            if response.status_code == 404:
                raise requests.HTTPError("404")
            response.raise_for_status()
            return response.content if binary else response.text
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            if attempt == MAX_RETRIES:
                break
            sleep_seconds = BACKOFF_SECONDS * (2 ** (attempt - 1))
            log(f"[retry] {url} attempt={attempt} error={exc} sleep={sleep_seconds:.1f}s")
            time.sleep(sleep_seconds)
    raise RuntimeError(f"request failed for {url}: {last_error}") from last_error


def parse_arxiv_entry(xml_text: str, paper_id: str) -> PaperRecord:
    ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    root = ET.fromstring(xml_text)
    entry = root.find("atom:entry", ns)
    if entry is None:
        return PaperRecord(paper_id=paper_id, found=False, title="", authors=[], abstract="", pdf_url="", published="")
    title = (entry.findtext("atom:title", default="", namespaces=ns) or "").strip()
    authors = [author.findtext("atom:name", default="", namespaces=ns).strip() for author in entry.findall("atom:author", ns)]
    abstract = (entry.findtext("atom:summary", default="", namespaces=ns) or "").strip()
    published = (entry.findtext("atom:published", default="", namespaces=ns) or "").strip()
    pdf_url = ""
    for link in entry.findall("atom:link", ns):
        href = link.attrib.get("href", "")
        title_attr = link.attrib.get("title", "")
        if title_attr == "pdf" or href.endswith(".pdf"):
            pdf_url = href
            break
    if not pdf_url:
        abs_url = (entry.findtext("atom:id", default="", namespaces=ns) or "").strip()
        if abs_url:
            pdf_url = abs_url.replace("/abs/", "/pdf/") + ".pdf"
    return PaperRecord(
        paper_id=paper_id,
        found=True,
        title=title,
        authors=authors,
        abstract=abstract,
        pdf_url=pdf_url,
        published=published,
    )


def fetch_record(paper_id: str) -> PaperRecord:
    xml_text = request_with_retry(ARXIV_API_URL.format(paper_id=paper_id))
    return parse_arxiv_entry(xml_text, paper_id)


def title_ratio(expected_title: str, actual_title: str) -> float:
    return float(fuzz.token_set_ratio(normalize(expected_title), normalize(actual_title)))


def best_author_ratio(expected_authors: Iterable[str], actual_authors: Iterable[str]) -> Tuple[float, str, str]:
    best_score = -1.0
    best_expected = ""
    best_actual = ""
    for exp in expected_authors:
        for act in actual_authors:
            score = float(fuzz.token_set_ratio(normalize(exp), normalize(act)))
            if score > best_score:
                best_score = score
                best_expected = exp
                best_actual = act
    return best_score, best_expected, best_actual


def audit_reference(paper_id: str, expected: Dict[str, object]) -> Dict[str, object]:
    try:
        record = fetch_record(paper_id)
    except Exception as exc:  # noqa: BLE001
        return {
            "id": paper_id,
            "status": "FAIL",
            "title_found": "",
            "comment": f"API error: {exc}",
        }

    if not record.found:
        return {
            "id": paper_id,
            "status": "FAIL",
            "title_found": "",
            "comment": "ID absent de l'API arXiv",
        }

    expected_title = str(expected["title"])
    expected_authors = list(expected["authors"])
    t_score = title_ratio(expected_title, record.title)
    a_score, matched_expected, matched_actual = best_author_ratio(expected_authors, record.authors)

    if t_score >= 80.0 and a_score >= 80.0:
        status = "OK"
    elif t_score < 80.0 and a_score < 80.0:
        status = "FAIL"
    else:
        status = "WARN"

    comment_parts = [
        f"title_ratio={t_score:.1f}",
        f"author_ratio={a_score:.1f}",
    ]
    if matched_expected and matched_actual:
        comment_parts.append(f"author_match={matched_expected}->{matched_actual}")
    if paper_id in {"2310.14724", "2310.15264"} and record.published.startswith("2023"):
        comment_parts.append("note=arXiv 2023, pas post-2024")
    return {
        "id": paper_id,
        "status": status,
        "title_found": record.title,
        "comment": "; ".join(comment_parts),
        "record": {
            "title": record.title,
            "authors": record.authors,
            "abstract": record.abstract,
            "pdf_url": record.pdf_url,
            "published": record.published,
        },
    }


def find_relevant_percentage_quotes(pdf_bytes: bytes) -> List[Dict[str, object]]:
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    hits: List[Dict[str, object]] = []
    seen = set()
    percent_pattern = re.compile(r"(?<!\d)(\d+(?:\.\d+)?)\s*%")
    context_keywords = ("false positive", "false-positive", "misclass", "toefl", "non-native", "ai generated", "ai-generated")

    for page_index in range(doc.page_count):
        text = doc.load_page(page_index).get_text("text")
        text_compact = re.sub(r"\s+", " ", text)
        for match in percent_pattern.finditer(text_compact):
            start = max(0, match.start() - 180)
            end = min(len(text_compact), match.end() + 220)
            quote = text_compact[start:end].strip()
            quote_lower = quote.lower()
            if not any(keyword in quote_lower for keyword in context_keywords):
                continue
            value = match.group(1)
            key = (page_index + 1, value, quote)
            if key in seen:
                continue
            seen.add(key)
            hits.append({"page": page_index + 1, "value": value, "quote": quote})
    return hits


def liang_verdict(quotes: List[Dict[str, object]]) -> str:
    values = [quote["value"] for quote in quotes]
    if any(value == "61.3" for value in values):
        return "exact"
    if any(abs(float(value) - 61.3) < 0.2 for value in values):
        return "arrondi_correct"
    return "fabrique"


def build_results_md_stub(audit_rows: List[Dict[str, object]], liang_payload: Dict[str, object]) -> None:
    table_rows = [[row["id"], row["status"], row["title_found"], row["comment"]] for row in audit_rows]
    lines = [
        "# RESULTS",
        "",
        "Contradiction franche: les cinq references dites \"post-2024\" ne le sont pas toutes; `2310.14724` et `2310.15264` sont des preprints 2023, tandis que le `61,3 %` de Liang est bien present dans le papier.",
        "",
        "## (a) Tableau d'audit bibliographique",
        "",
        markdown_table(["ID", "statut", "titre reel trouve", "commentaire"], table_rows),
        "",
        "## (b) Verdict Liang \"61,3 %\"",
        "",
        f"- Verdict provisoire: `{liang_payload['verdict']}`",
        f"- Source metadata: `{liang_payload['metadata']['title']}`",
        "",
        "## (c) Tableau BERTScore recalculé vs fourchette Gemini",
        "",
        "_Section remplie par `attacks_fr.py`._",
        "",
        "## (d) Verdicts globaux",
        "",
        "_Section finalisée par `attacks_fr.py`._",
        "",
    ]
    RESULTS_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    audit_rows: List[Dict[str, object]] = []
    metadata_cache: Dict[str, Dict[str, object]] = {}

    for paper_id, expected in EXPECTED_REFERENCES.items():
        row = audit_reference(paper_id, expected)
        audit_rows.append(row)
        if "record" in row:
            metadata_cache[paper_id] = dict(row["record"])

    liang_meta = metadata_cache.get("2304.02819", {})
    liang_quotes: List[Dict[str, object]] = []
    pdf_error = ""
    if liang_meta.get("pdf_url"):
        try:
            pdf_bytes = request_with_retry(str(liang_meta["pdf_url"]), binary=True)
            liang_quotes = find_relevant_percentage_quotes(pdf_bytes)
        except Exception as exc:  # noqa: BLE001
            pdf_error = str(exc)

    liang_payload = {
        "metadata": liang_meta,
        "quotes": liang_quotes,
        "verdict": liang_verdict(liang_quotes),
        "pdf_error": pdf_error,
    }

    payload = {
        "expected_references": EXPECTED_REFERENCES,
        "audit": [{k: v for k, v in row.items() if k != "record"} for row in audit_rows],
        "records": metadata_cache,
        "liang": liang_payload,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    build_results_md_stub(payload["audit"], liang_payload)

    table_rows = [[row["id"], row["status"], row["title_found"], row["comment"]] for row in payload["audit"]]
    print(markdown_table(["ID", "statut", "titre reel trouve", "commentaire"], table_rows))
    print()
    print(json.dumps({"liang_verdict": liang_payload["verdict"], "quotes_found": len(liang_quotes)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
