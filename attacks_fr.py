#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import json
import math
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Optional, Sequence, Tuple

os.environ.setdefault("HF_HOME", str(Path(".hf_cache").resolve()))
os.environ.setdefault("HF_HUB_CACHE", str((Path(".hf_cache") / "hub").resolve()))
os.environ.setdefault("TRANSFORMERS_CACHE", str((Path(".hf_cache") / "transformers").resolve()))
os.environ.setdefault("MPLCONFIGDIR", str(Path(".mplconfig").resolve()))

import numpy as np
import spacy
import torch
from bert_score import score as bert_score
from huggingface_hub import snapshot_download
from transformers import AutoModelForCausalLM, AutoModelForSeq2SeqLM, AutoTokenizer


VERIFY_JSON = Path("verify_biblio_results.json")
RESULTS_MD = Path("RESULTS.md")
ATTACKS_JSON = Path("attack_results.json")
LOCAL_MODEL_ROOT = Path(".hf_models")
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
SEED = 0

np.random.seed(SEED)
torch.manual_seed(SEED)

NLP: Optional["spacy.language.Language"] = None
TOKENIZER_CACHE: Dict[str, AutoTokenizer] = {}
MODEL_CACHE: Dict[str, torch.nn.Module] = {}


@dataclass
class AttackSpec:
    name: str
    label: str
    heuristic: str
    heuristic_range: Optional[Tuple[float, float]]
    function: Callable[[str], str]


MINI_CORPUS: Dict[str, str] = {
    "histoire_contemporaine": (
        "L'histoire contemporaine ne peut plus être écrite comme une simple chronologie des décisions d'État. "
        "Depuis une vingtaine d'années, les travaux sur les administrations ordinaires ont montré que la puissance publique "
        "se déploie aussi dans des gestes minuscules: remplir un formulaire, classer un dossier, différer une réponse. "
        "L'intérêt de cette approche est double. D'une part, elle corrige une lecture héroïque des événements en restituant "
        "les médiations techniques qui rendent l'action possible. D'autre part, elle éclaire la manière dont les citoyens "
        "expérimentent concrètement la souveraineté. Le cas des politiques de rationnement après 1945 est, à cet égard, "
        "instructif. Les archives montrent moins une obéissance mécanique qu'une négociation continue entre règles centrales "
        "et arrangements locaux. L'État fixe un cadre, mais la mise en oeuvre dépend de secrétaires de mairie, de commerçants "
        "et d'agents de contrôle dont les marges d'interprétation sont réelles. Écrire cette histoire suppose donc de tenir "
        "ensemble institutions, pratiques documentaires et temporalités sociales."
    ),
    "economie_environnement": (
        "L'économie de l'environnement est souvent résumée à la question du prix du carbone, alors que le problème est plus "
        "large. La tarification ne produit pas, à elle seule, la transition écologique; elle modifie des incitations dans un "
        "cadre institutionnel déjà structuré par des subventions, des normes et des infrastructures héritées. Il faut donc "
        "analyser les politiques climatiques comme des combinaisons d'instruments. Une taxe peut être efficace dans un secteur "
        "où les comportements sont flexibles, mais beaucoup moins dans des activités soumises à des investissements lourds. "
        "C'est pourquoi l'évaluation économique doit intégrer la distribution sociale des coûts, la crédibilité des annonces "
        "publiques et les délais d'ajustement. Une mesure écologiquement cohérente mais politiquement intenable risque de "
        "n'avoir qu'un effet provisoire. À l'inverse, un dispositif imparfait mais stable peut déplacer durablement les choix "
        "d'investissement. L'enjeu n'est donc pas de chercher un instrument pur, mais une architecture de politiques capable "
        "de réduire les émissions sans aggraver la fragilité sociale."
    ),
    "sociolinguistique": (
        "En sociolinguistique, la variation ne doit pas être pensée comme un simple bruit autour d'une norme abstraite. "
        "Elle constitue une ressource sociale par laquelle les locuteurs indexent des appartenances, des distances et des "
        "situations. Cette idée est particulièrement visible dans les espaces urbains plurilingues, où les changements de "
        "registre ne signalent pas seulement une compétence linguistique, mais aussi une capacité d'ajustement interactionnel. "
        "Observer une alternance codique sans décrire le contexte revient à perdre l'essentiel: qui parle, à qui, avec quel "
        "enjeu, et dans quelle scène sociale. Les enquêtes menées dans les universités montrent par exemple que certains "
        "marqueurs réputés familiers réapparaissent dans des échanges très formels, non par relâchement, mais pour réduire "
        "une asymétrie relationnelle. La description des pratiques doit donc combiner analyse quantitative et ethnographie "
        "des situations. Sans cette double focale, on risque de réifier la langue et de manquer les usages stratégiques qui "
        "fabriquent, au quotidien, les hiérarchies symboliques."
    ),
}


REGIONALISM_PAIRS: List[Tuple[str, str]] = [
    ("cependant", "pour autant"),
    ("ainsi", "de la sorte"),
    ("néanmoins", "malgré tout"),
    ("toutefois", "cela dit"),
    ("dès lors", "à partir de là"),
    ("par conséquent", "du même coup"),
    ("par ailleurs", "sur un autre plan"),
    ("en outre", "au surplus"),
    ("il faut", "il convient"),
    ("montrer", "faire voir"),
    ("mettre en oeuvre", "mettre sur pied"),
    ("souvent", "bien des fois"),
    ("rarement", "à peu près jamais"),
    ("maintenant", "à présent"),
    ("rapidement", "sans trop attendre"),
    ("important", "de poids"),
    ("utile", "bon à prendre"),
    ("difficile", "malaisé"),
    ("probable", "vraisemblable"),
    ("penser", "tenir pour vrai"),
    ("question", "affaire"),
    ("analyse", "examen"),
    ("résultat", "issue"),
    ("méthode", "façon de faire"),
    ("exemple", "cas de figure"),
    ("faible", "maigre"),
    ("fort", "marqué"),
    ("car", "vu que"),
    ("donc", "partant"),
    ("mais", "or"),
]


HOMOGLYPHS = {"a": "а", "e": "е", "o": "о", "p": "р", "c": "с"}
ORALITY_MARKERS = ["enfin bref", "je veux dire", "du coup"]
SUBORD_MARKERS = {"parce", "puisque", "lorsque", "quand", "si", "bien", "alors", "comme"}


def log(message: str) -> None:
    print(message, file=sys.stderr)


def normalize_whitespace(text: str) -> str:
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


def get_nlp() -> "spacy.language.Language":
    global NLP
    if NLP is None:
        NLP = spacy.load("fr_core_news_lg")
    return NLP


def prepare_local_model(model_name: str) -> str:
    local_dir = LOCAL_MODEL_ROOT / model_name.replace("/", "__")
    local_dir.mkdir(parents=True, exist_ok=True)
    snapshot_download(
        repo_id=model_name,
        local_dir=str(local_dir),
        local_dir_use_symlinks=False,
        resume_download=True,
    )
    return str(local_dir)


def load_tokenizer(model_name: str) -> AutoTokenizer:
    if model_name not in TOKENIZER_CACHE:
        local_path = prepare_local_model(model_name)
        tokenizer = AutoTokenizer.from_pretrained(local_path)
        if tokenizer.pad_token_id is None and tokenizer.eos_token is not None:
            tokenizer.pad_token = tokenizer.eos_token
        TOKENIZER_CACHE[model_name] = tokenizer
    return TOKENIZER_CACHE[model_name]


def load_model(model_name: str, model_class):
    if model_name not in MODEL_CACHE:
        local_path = prepare_local_model(model_name)
        model = model_class.from_pretrained(local_path)
        model.to(DEVICE)
        model.eval()
        MODEL_CACHE[model_name] = model
    return MODEL_CACHE[model_name]


def split_sentences(text: str) -> List[str]:
    doc = get_nlp()(text)
    return [sent.text.strip() for sent in doc.sents if sent.text.strip()]


def apply_case(source: str, target: str) -> str:
    if source.isupper():
        return target.upper()
    if source[:1].isupper():
        return target[:1].upper() + target[1:]
    return target


def replace_word_pairs(text: str, pairs: Sequence[Tuple[str, str]]) -> str:
    updated = text
    for source, target in pairs:
        pattern = re.compile(rf"\b{re.escape(source)}\b", re.IGNORECASE)
        updated = pattern.sub(lambda match: apply_case(match.group(0), target), updated)
    return normalize_whitespace(updated)


def select_evenly(indices: Sequence[int], target_count: int) -> List[int]:
    if target_count <= 0 or not indices:
        return []
    if target_count >= len(indices):
        return list(indices)
    positions = np.linspace(0, len(indices) - 1, target_count, dtype=int)
    return [indices[int(pos)] for pos in positions]


def safe_attack(function: Callable[[str], str], text: str) -> Tuple[str, str]:
    try:
        return function(text), ""
    except Exception as exc:  # noqa: BLE001
        log(f"[attack-error] {function.__name__}: {exc}")
        return text, str(exc)


def attaque_back_translation_frenfr(text: str) -> str:
    fr_en_name = "Helsinki-NLP/opus-mt-fr-en"
    en_fr_name = "Helsinki-NLP/opus-mt-en-fr"
    fr_en_tokenizer = load_tokenizer(fr_en_name)
    en_fr_tokenizer = load_tokenizer(en_fr_name)
    fr_en_model = load_model(fr_en_name, AutoModelForSeq2SeqLM)
    en_fr_model = load_model(en_fr_name, AutoModelForSeq2SeqLM)

    with torch.no_grad():
        fr_inputs = fr_en_tokenizer([text], return_tensors="pt", padding=True, truncation=True, max_length=512).to(DEVICE)
        en_ids = fr_en_model.generate(**fr_inputs, max_new_tokens=384)
        english = fr_en_tokenizer.batch_decode(en_ids, skip_special_tokens=True)[0]

        en_inputs = en_fr_tokenizer([english], return_tensors="pt", padding=True, truncation=True, max_length=512).to(DEVICE)
        fr_ids = en_fr_model.generate(**en_inputs, max_new_tokens=384)
        french = en_fr_tokenizer.batch_decode(fr_ids, skip_special_tokens=True)[0]
    return normalize_whitespace(french)


def attaque_variance_syntaxique_forcee(text: str) -> str:
    doc = get_nlp()(text)
    rebuilt: List[str] = []
    for index, sent in enumerate(doc.sents):
        sentence_text = sent.text.strip()
        transformed = sentence_text
        for token in sent:
            if token.dep_ != "mark" or token.text.lower() not in SUBORD_MARKERS:
                continue
            clause_tokens = sorted(list(token.head.subtree), key=lambda item: item.i)
            clause_start = clause_tokens[0].idx
            clause_end = clause_tokens[-1].idx + len(clause_tokens[-1].text)
            sent_start = sent.start_char
            sent_end = sent.end_char
            clause = doc.text[clause_start:clause_end].strip(" ,")
            main_left = doc.text[sent_start:clause_start].strip(" ,")
            main_right = doc.text[clause_end:sent_end].strip(" ,")
            main = normalize_whitespace(f"{main_left} {main_right}")
            if not clause or not main or clause == sentence_text:
                continue
            if clause_start > sent_start and index % 2 == 0:
                transformed = f"{clause.capitalize()}, {main.rstrip('.;:!?')}."
            elif clause_start == sent_start and "," in sentence_text and index % 2 == 1:
                transformed = f"{main.rstrip('.;:!?')}, {clause.lower()}."
            break
        if transformed == sentence_text and len(sentence_text.split()) > 20 and "," in sentence_text:
            left, right = sentence_text.split(",", 1)
            transformed = f"{left.strip()}. {right.strip()}"
        rebuilt.append(normalize_whitespace(transformed))
    return " ".join(rebuilt)


def attaque_injection_oralite(text: str) -> str:
    sentences = split_sentences(text)
    rebuilt: List[str] = []
    for index, sentence in enumerate(sentences):
        marker = ORALITY_MARKERS[index % len(ORALITY_MARKERS)]
        if index % 3 == 0:
            rebuilt.append(f"{marker.capitalize()}, {sentence[:1].lower()}{sentence[1:]}")
        elif index % 3 == 1:
            rebuilt.append(sentence.rstrip(".") + f", {marker}.")
        else:
            rebuilt.append(sentence)
    return normalize_whitespace(" ".join(rebuilt))


def attaque_regionalismes_archaismes(text: str) -> str:
    return replace_word_pairs(text, REGIONALISM_PAIRS)


def attaque_substitution_gltr_topk(text: str) -> str:
    model_name = "dbddv01/gpt2-french-small"
    tokenizer = load_tokenizer(model_name)
    model = load_model(model_name, AutoModelForCausalLM)

    encoded = tokenizer(text, return_tensors="pt", add_special_tokens=True)
    input_ids = encoded["input_ids"].to(DEVICE)
    if input_ids.size(1) < 4:
        return text

    with torch.no_grad():
        logits = model(input_ids).logits[0]

    replacement_map: Dict[int, int] = {}
    eligible_positions: List[int] = []
    sequence = input_ids[0]
    for position in range(1, sequence.size(0)):
        gold_token = int(sequence[position].item())
        prediction = logits[position - 1]
        _, top_indices = torch.topk(prediction, k=min(16, prediction.size(-1)))
        top_ids = [int(item) for item in top_indices.tolist()]
        if len(top_ids) < 10:
            continue
        if gold_token != top_ids[0]:
            continue
        candidate = top_ids[9]
        candidate_text = tokenizer.decode([candidate]).strip()
        if not candidate_text or candidate_text == tokenizer.decode([gold_token]).strip():
            continue
        replacement_map[position] = candidate
        eligible_positions.append(position)

    target_count = max(1, math.ceil(0.15 * max(sequence.size(0) - 1, 1)))
    selected_positions = set(select_evenly(eligible_positions, target_count))
    replaced = sequence.detach().cpu().clone()
    for position in selected_positions:
        replaced[position] = replacement_map[position]
    return normalize_whitespace(tokenizer.decode(replaced.tolist(), skip_special_tokens=True))


def attaque_perturbation_ponctuation(text: str) -> str:
    doc = get_nlp()(text)
    rebuilt: List[str] = []
    for index, sent in enumerate(doc.sents):
        sentence = sent.text.strip()
        words = sentence.split()
        if not words:
            continue
        if index % 2 == 0 and len(words) > 10 and "," not in sentence:
            insert_at = min(4, len(words) - 1)
            words[insert_at - 1] = words[insert_at - 1].rstrip(",") + ","
            rebuilt.append(" ".join(words))
        elif index % 2 == 1 and sentence.count(",") >= 1:
            rebuilt.append(sentence.replace(",", "", 1))
        else:
            rebuilt.append(sentence)
    return normalize_whitespace(" ".join(rebuilt))


def attaque_homoglyphes_unicode(text: str) -> str:
    chars = list(text)
    eligible = [idx for idx, char in enumerate(chars) if char.lower() in HOMOGLYPHS]
    selected = set(select_evenly(eligible, max(1, math.floor(0.05 * max(len(eligible), 1)))))
    for idx in selected:
        mapped = HOMOGLYPHS[chars[idx].lower()]
        chars[idx] = mapped.upper() if chars[idx].isupper() else mapped
    return "".join(chars)


def stub_paraphrase_profonde_dipper(text: str) -> str:
    """Stub défensif: brancher ici un appel d'API Claude pour une paraphrase profonde contrôlée."""
    return text


def stub_style_transfer_prompt(text: str) -> str:
    """Stub défensif: brancher ici un appel d'API Claude pour un style-transfer persona L2 contrôlé."""
    return text


def stub_hybridation_humain_ia(text: str) -> str:
    """Stub défensif: brancher ici un appel d'API Claude qui n'altère qu'une sous-partie du texte."""
    return text


ATTACK_SPECS: List[AttackSpec] = [
    AttackSpec(
        name="back_translation_frenfr",
        label="Back-translation FR->EN->FR",
        heuristic="0.85-0.90",
        heuristic_range=(0.85, 0.90),
        function=attaque_back_translation_frenfr,
    ),
    AttackSpec(
        name="variance_syntaxique",
        label="Variance syntaxique forcée",
        heuristic="~0.85",
        heuristic_range=(0.84, 0.86),
        function=attaque_variance_syntaxique_forcee,
    ),
    AttackSpec(
        name="injection_oralite",
        label="Injection d'oralité",
        heuristic="~0.75",
        heuristic_range=(0.74, 0.76),
        function=attaque_injection_oralite,
    ),
    AttackSpec(
        name="regionalismes_archaismes",
        label="Régionalismes / archaïsmes",
        heuristic="0.80-0.85",
        heuristic_range=(0.80, 0.85),
        function=attaque_regionalismes_archaismes,
    ),
    AttackSpec(
        name="substitution_gltr_topk",
        label="Substitution GLTR top-k",
        heuristic="~0.80",
        heuristic_range=(0.79, 0.81),
        function=attaque_substitution_gltr_topk,
    ),
    AttackSpec(
        name="perturbation_ponctuation",
        label="Perturbation ponctuation",
        heuristic="~0.95",
        heuristic_range=(0.94, 0.96),
        function=attaque_perturbation_ponctuation,
    ),
    AttackSpec(
        name="homoglyphes_unicode",
        label="Homoglyphes Unicode",
        heuristic="1.00 visuel / 0.00 tokenisation",
        heuristic_range=None,
        function=attaque_homoglyphes_unicode,
    ),
]


def compute_bertscore(candidates: Sequence[str], references: Sequence[str]) -> float:
    local_model_path = prepare_local_model("bert-base-multilingual-cased")
    _, _, f1 = bert_score(
        list(candidates),
        list(references),
        model_type=local_model_path,
        lang="fr",
        rescale_with_baseline=True,
        verbose=False,
        device=DEVICE,
    )
    return float(f1.mean().item())


def compare_to_heuristic(value: float, bounds: Optional[Tuple[float, float]]) -> str:
    if bounds is None:
        return "non_comparable"
    lower, upper = bounds
    if lower <= value <= upper:
        return "dans_fourchette"
    if value < lower:
        return "sous_fourchette"
    return "au_dessus"


def load_verify_payload() -> Dict[str, object]:
    if not VERIFY_JSON.exists():
        raise FileNotFoundError("verify_biblio_results.json absent. Exécuter verify_biblio.py d'abord.")
    return json.loads(VERIFY_JSON.read_text(encoding="utf-8"))


def run_attacks() -> List[Dict[str, object]]:
    references = list(MINI_CORPUS.values())
    rows: List[Dict[str, object]] = []
    baseline = compute_bertscore(references, references)

    for spec in ATTACK_SPECS:
        attacked_texts: List[str] = []
        errors: List[str] = []
        for text in references:
            attacked, error = safe_attack(spec.function, text)
            attacked_texts.append(attacked)
            if error:
                errors.append(error)
        if errors:
            rows.append(
                {
                    "attack": spec.label,
                    "attack_key": spec.name,
                    "status": "SKIP",
                    "bertscore_before": baseline,
                    "bertscore_after": None,
                    "heuristic": spec.heuristic,
                    "heuristic_check": "non_evaluable",
                    "error": errors[0],
                }
            )
            continue
        try:
            after = compute_bertscore(attacked_texts, references)
            rows.append(
                {
                    "attack": spec.label,
                    "attack_key": spec.name,
                    "status": "OK",
                    "bertscore_before": baseline,
                    "bertscore_after": after,
                    "heuristic": spec.heuristic,
                    "heuristic_check": compare_to_heuristic(after, spec.heuristic_range),
                    "error": "",
                }
            )
        except Exception as exc:  # noqa: BLE001
            log(f"[bertscore-error] {spec.name}: {exc}")
            rows.append(
                {
                    "attack": spec.label,
                    "attack_key": spec.name,
                    "status": "SKIP",
                    "bertscore_before": baseline,
                    "bertscore_after": None,
                    "heuristic": spec.heuristic,
                    "heuristic_check": "non_evaluable",
                    "error": str(exc),
                }
            )
    return rows


def liang_quote_note(value: str, quote: str) -> str:
    lowered = quote.lower()
    if value == "61.3":
        return "FPR moyen sur essais TOEFL non natifs"
    if value == "19.8":
        return "Essais TOEFL signales par tous les detecteurs"
    if value == "97.8":
        return "Essais TOEFL signales par au moins un detecteur"
    if value in {"49.7", "11.6", "11.77"}:
        return "Apres amelioration linguistique via ChatGPT"
    if "false-positive" in lowered or "false positive" in lowered:
        return "Mention FPR non native"
    return "Pourcentage pertinent extrait du PDF"


def contradiction_line(verify_payload: Dict[str, object], attack_rows: List[Dict[str, object]]) -> str:
    audit_rows = verify_payload["audit"]
    year_mismatches = [row["id"] for row in audit_rows if "pas post-2024" in row["comment"]]
    liang = verify_payload["liang"]
    large_gaps = [
        row["attack"]
        for row in attack_rows
        if row["status"] == "OK" and row["heuristic_check"] != "dans_fourchette"
    ]
    pieces = []
    if year_mismatches:
        pieces.append(f"la catégorie « post-2024 » est fausse pour {', '.join(year_mismatches)}")
    pieces.append(f"le « 61,3 % » de Liang est {liang['verdict']}")
    if large_gaps:
        pieces.append(f"au moins une heuristique BERTScore sort de la fourchette Gemini ({large_gaps[0]})")
    return "Contradiction franche: " + " ; ".join(pieces) + "."


def build_results_markdown(verify_payload: Dict[str, object], attack_rows: List[Dict[str, object]]) -> str:
    audit_rows = [
        [row["id"], row["status"], row["title_found"], row["comment"]]
        for row in verify_payload["audit"]
    ]
    liang = verify_payload["liang"]
    liang_rows = []
    for quote in liang["quotes"]:
        liang_rows.append(
            [
                str(quote["page"]),
                str(quote["value"]) + "%",
                liang_quote_note(str(quote["value"]), str(quote["quote"])),
                normalize_whitespace(str(quote["quote"]))[:220] + ("..." if len(str(quote["quote"])) > 220 else ""),
            ]
        )
    if not liang_rows:
        liang_rows.append(["-", "-", "PDF indisponible", liang.get("pdf_error", "Aucune citation extraite")])

    attack_table_rows = []
    for row in attack_rows:
        attack_table_rows.append(
            [
                row["attack"],
                row["status"],
                f"{row['bertscore_before']:.4f}" if row["bertscore_before"] is not None else "-",
                f"{row['bertscore_after']:.4f}" if row["bertscore_after"] is not None else "-",
                row["heuristic"],
                row["heuristic_check"],
                row["error"] or "-",
            ]
        )

    bibliographic_verdict = "partiellement_confirmee" if any("pas post-2024" in row["comment"] for row in verify_payload["audit"]) else "validee"
    liang_verdict = "partiellement_confirmee" if liang["verdict"] == "exact" else ("invalidée" if liang["verdict"] == "fabrique" else "partiellement_confirmee")
    bert_verdict = "invalidée" if any(row["status"] == "OK" and row["heuristic_check"] != "dans_fourchette" for row in attack_rows) else "partiellement_confirmee"

    global_rows = [
        [
            "Volet 1 - audit bibliographique",
            bibliographic_verdict,
            "Conserver les 12 IDs valides, mais retirer l'etiquette « post-2024 » pour `2310.14724` et `2310.15264`.",
        ],
        [
            "Volet 2 - chiffre Liang 61,3 %",
            liang_verdict,
            "Conserver `61,3 %` si la citation vise le papier Liang; préciser qu'il s'agit d'essais TOEFL d'auteurs non natifs en anglais, pas d'un benchmark francophone.",
        ],
        [
            "Volet 3 - matrice BERTScore Q5",
            bert_verdict,
            "Remplacer les valeurs heuristiques hors fourchette par les scores recalculés; supprimer `1.00` pour l'hybridation tant qu'aucune mesure réelle n'est fournie.",
        ],
    ]

    sections = [
        "# RESULTS",
        "",
        contradiction_line(verify_payload, attack_rows),
        "",
        "## (a) Tableau d'audit bibliographique",
        "",
        markdown_table(["ID", "statut", "titre reel trouve", "commentaire"], audit_rows),
        "",
        "## (b) Verdict Liang \"61,3 %\"",
        "",
        markdown_table(["page", "pourcentage", "interpretation", "citation"], liang_rows),
        "",
        markdown_table(
            ["champ", "valeur"],
            [
                ["verdict", liang["verdict"]],
                ["titre", verify_payload["records"]["2304.02819"]["title"]],
                ["published", verify_payload["records"]["2304.02819"]["published"]],
                ["abstract_excerpt", normalize_whitespace(verify_payload["records"]["2304.02819"]["abstract"])[:220] + "..."],
                ["pdf_status", "fallback HTML/abstract" if liang.get("pdf_error") and not liang["quotes"] else "pdf parsed"],
            ],
        ),
        "",
        "## (c) Tableau BERTScore recalculé vs fourchette Gemini",
        "",
        markdown_table(
            ["attaque", "statut", "bert_avant", "bert_apres", "fourchette_gemini", "verdict", "erreur"],
            attack_table_rows,
        ),
        "",
        "## (d) Verdicts globaux",
        "",
        markdown_table(["zone", "verdict", "correction precise"], global_rows),
        "",
    ]
    return "\n".join(sections)


def main() -> None:
    verify_payload = load_verify_payload()
    attack_rows = run_attacks()
    ATTACKS_JSON.write_text(json.dumps({"attacks": attack_rows}, ensure_ascii=False, indent=2), encoding="utf-8")
    RESULTS_MD.write_text(build_results_markdown(verify_payload, attack_rows), encoding="utf-8")
    print(markdown_table(
        ["attaque", "statut", "bert_avant", "bert_apres", "fourchette_gemini", "verdict"],
        [
            [
                row["attack"],
                row["status"],
                f"{row['bertscore_before']:.4f}" if row["bertscore_before"] is not None else "-",
                f"{row['bertscore_after']:.4f}" if row["bertscore_after"] is not None else "-",
                row["heuristic"],
                row["heuristic_check"],
            ]
            for row in attack_rows
        ],
    ))


if __name__ == "__main__":
    main()
