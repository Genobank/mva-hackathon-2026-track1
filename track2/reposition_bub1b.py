#!/usr/bin/env python3
"""Public, genome-free Track 2 map for BUB1B MVA1 (PROBAND01).

Inputs are UniProt accession O60566, Ensembl ENST00000287598, and published
literature. No FASTQ/BAM/VCF.
Run: python3 reposition_bub1b.py

Prints:
  1. Remaining protein after NMD-expected p.Leu737Ter (exon 17/23).
  2. Ranked market-approved candidates, R index, sensitivity, reject list.
  3. Optional OpenTargets / ChEMBL lookup (network; skipped if offline).
"""
from __future__ import annotations

import json
import urllib.error
import urllib.request

UNIPROT = "O60566"
TRANSCRIPT = "ENST00000287598"
STOP = 737  # p.Leu737Ter: escape polypeptide is 1..736
STOP_EXON = (17, 23)
K668 = 668
KINASE = (766, 1050)
N1002 = 1002
PROTEIN_LEN = 1050

# R = 100 * (0.35 M + 0.25 G + 0.20 P + 0.20 L) * (1 - C)
# Not a clinical probability. Weights frozen before scoring.
WEIGHTS = {"M": 0.35, "G": 0.25, "P": 0.20, "L": 0.20}


def r_index(M: float, G: float, P: float, L: float, C: float) -> int:
    # Integer-percent inner score, then half-up. Avoids 52.4999... truncating to 52.
    inner = 35 * M + 25 * G + 20 * P + 20 * L
    return int(inner * (1 - C) + 0.5 + 1e-9)


CANDIDATES = [
    {
        "rank": 1,
        "name": "nicotinamide",
        "M": 1.00,
        "G": 1.00,
        "P": 0.40,
        "L": 0.70,
        "C": 0.15,
        "research_analog": "nicotinamide riboside / NMN",
        "label": "licensed vitamin B3; NR/NMN are NAD+ precursors in human trials",
        "axis": "SIRT2 deacetylates BUBR1 K668 and stabilizes remaining protein (North 2014 EMBO J)",
        "child_match": "K668 is on the default remaining protein (full-length N1002K) and on any NMD-escape stub",
    },
    {
        "rank": 2,
        "name": "metformin",
        "M": 0.40,
        "G": 0.30,
        "P": 0.55,
        "L": 1.00,
        "C": 0.00,
        "research_analog": None,
        "label": "FDA AMPK activator; pediatric type 2 diabetes use",
        "axis": "AMPK / energy stress of aneuploidy (Tang 2011 Cell); milder mTORC1 brake. Not the high-dose AICAR killer from the same paper.",
        "child_match": "metabolic buffer, not a cytotoxic selector against mosaic cells",
    },
    {
        "rank": 3,
        "name": "sirolimus",
        "M": 0.60,
        "G": 0.50,
        "P": 0.85,
        "L": 1.00,
        "C": 0.40,
        "research_analog": "everolimus",
        "label": "FDA mTORC1 inhibitor; pediatric TSC / transplant use",
        "axis": "mTORC1 hyperactivity tracks sarcopenia in BubR1 allelic-series mice (Sieben 2020 JCI)",
        "child_match": "skeletal muscle atrophy and failure to thrive in the challenge phenotype; RMS history sets C=0.40",
    },
]

NOT_RANKED = [
    {
        "name": "dasatinib + quercetin (senolytics)",
        "M": 0.65,
        "G": 0.20,
        "P": 0.45,
        "L": 0.30,
        "C": 0.55,
        "axis": "Baker 2011/2016 Nature: clearing p16+ senescent cells in BubR1H/H mice",
        "why_not": "no pediatric MVA label; cancer-predisposition genome plus rhabdomyosarcoma",
    },
    {
        "name": "ivermectin",
        "M": 0.25,
        "G": 0.10,
        "P": 0.15,
        "L": 0.85,
        "C": 0.55,
        "axis": "Ashraf 2015/2016: taxol-pocket tubulin binding, polymerization promoter, reversible mitotic arrest. Human Stromectol.",
        "why_not": "taxane-class freeze of microtubule dynamics on a weak SAC; labeled Cmax ~35-54 nM vs micromolar tubulin assays",
    },
]

REJECTS = [
    {
        "class": "microtubule poisons",
        "examples": ["vincristine", "vinblastine", "paclitaxel"],
        "reason": "weaken attachment error-correction; not a constitutional MVA therapy",
    },
    {
        "class": "MPS1 / Aurora / CENP-E inhibitors",
        "examples": ["reversine", "alisertib"],
        "reason": "silence the checkpoint that is already weak",
    },
    {
        "class": "aneuploid-cell killers",
        "examples": ["17-AAG", "high-dose AICAR"],
        "reason": "select against aneuploid cells; this genome is constitutionally mosaic",
    },
    {
        "class": "senolytics",
        "examples": ["dasatinib + quercetin", "INK-ATTAC"],
        "reason": "founding BubR1H/H pharmacology; not a constitutional pediatric therapy on an RMS background",
    },
    {
        "class": "microtubule stabilizer (taxane-site class)",
        "examples": ["ivermectin"],
        "reason": "promotes tubulin polymerization (Ashraf 2015/2016); freezes error-correction a BUBR1-low SAC cannot police; labeled human Cmax is nanomolar",
    },
]


def remaining_protein() -> dict:
    kept = STOP - 1
    nam = CANDIDATES[0]
    met = CANDIDATES[1]
    siro = CANDIDATES[2]
    return {
        "uniprot": UNIPROT,
        "transcript": TRANSCRIPT,
        "stop": STOP,
        "stop_exon": f"{STOP_EXON[0]}/{STOP_EXON[1]}",
        "nmd_expected": True,
        "nmd_rule": "PTC in exon 17 of 23; last exon-exon junction is 6 exons downstream (50-nt rule)",
        "default_remaining_protein": "full-length p.Asn1002Lys (missense allele)",
        "escape_polypeptide": {
            "kept_residues": kept,
            "lost_residues": PROTEIN_LEN - kept,
            "k668_remaining": K668 <= kept,
            "kinase_remaining": KINASE[0] <= kept,
        },
        "missense_allele": {
            "residue": N1002,
            "in_kinase": KINASE[0] <= N1002 <= KINASE[1],
            "k668_remaining": True,
            "full_length": True,
        },
        "track1_cosic_on_escape_polypeptide": {
            "eiip_fc_ratio_truncation": 0.810,
            "piezo_fc_ratio_truncation": 0.534,
            "note": "Maps the NMD-escape stub if produced. Not proof of expression. N-terminal resonance mostly intact; kinase-scale piezo harmonic halved.",
        },
        "R": {
            "formula": "100 * (0.35 M + 0.25 G + 0.20 P + 0.20 L) * (1 - C)",
            "nicotinamide": r_index(nam["M"], nam["G"], nam["P"], nam["L"], nam["C"]),
            "metformin": r_index(met["M"], met["G"], met["P"], met["L"], met["C"]),
            "sirolimus": r_index(siro["M"], siro["G"], siro["P"], siro["L"], siro["C"]),
            "sirolimus_if_C_zero": r_index(siro["M"], siro["G"], siro["P"], siro["L"], 0.0),
            "senolytics_not_ranked": r_index(0.65, 0.20, 0.45, 0.30, 0.55),
            "ivermectin_not_ranked": r_index(0.25, 0.10, 0.15, 0.85, 0.55),
        },
    }


def opentargets_bub1b() -> dict:
    """ENSG00000156970. Schema varies by API version; record errors instead of guessing drugs."""
    q = {
        "query": """query { target(ensemblId: \"ENSG00000156970\") { id approvedSymbol } }"""
    }
    req = urllib.request.Request(
        "https://api.platform.opentargets.org/api/v4/graphql",
        data=json.dumps(q).encode(),
        headers={"Content-Type": "application/json", "User-Agent": "genobank-track2/2"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.loads(r.read().decode())
    except Exception as e:
        return {"error": str(e)}


def main() -> None:
    for row in CANDIDATES:
        row["R"] = r_index(row["M"], row["G"], row["P"], row["L"], row["C"])
    for row in NOT_RANKED:
        row["R"] = r_index(row["M"], row["G"], row["P"], row["L"], row["C"])
    out = {
        "disclaimer": "Research hypothesis. Not medical care. Genome gated.",
        "gene": "BUB1B",
        "disease": "Mosaic variegated aneuploidy syndrome 1",
        "remaining_protein": remaining_protein(),
        "candidates": CANDIDATES,
        "not_ranked": NOT_RANKED,
        "rejects": REJECTS,
        "opentargets": opentargets_bub1b(),
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
