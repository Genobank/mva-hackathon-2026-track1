#!/usr/bin/env python3
"""Public, genome-free Track 2 map for BUB1B MVA1 (PROBAND01).

Inputs are UniProt accession O60566 and published literature. No FASTQ/BAM/VCF.
Run: python3 reposition_bub1b.py

Prints:
  1. Remaining-chain sites after p.Leu737Ter (kinase gone, K668 stays).
  2. Ranked market-approved candidates and an explicit reject list.
  3. Optional OpenTargets / ChEMBL lookup (network; skipped if offline).
"""
from __future__ import annotations

import json
import urllib.error
import urllib.request

UNIPROT = "O60566"
STOP = 737  # p.Leu737Ter: remaining chain is 1..736
K668 = 668
KINASE = (766, 1050)
N1002 = 1002

CANDIDATES = [
    {
        "rank": 1,
        "name": "nicotinamide",
        "research_analog": "nicotinamide riboside / NMN",
        "label": "licensed vitamin B3; NR/NMN are NAD+ precursors in human trials",
        "axis": "SIRT2 deacetylates BUBR1 K668 and stabilizes remaining protein (North 2014 EMBO J)",
        "child_match": "K668 is on the truncated chain (668 < 737) and on the missense allele",
    },
    {
        "rank": 2,
        "name": "sirolimus",
        "research_analog": "everolimus",
        "label": "FDA mTORC1 inhibitor; pediatric TSC / transplant use",
        "axis": "mTORC1 hyperactivity tracks sarcopenia in BubR1 allelic-series mice (Sieben 2020 JCI)",
        "child_match": "skeletal muscle atrophy and failure to thrive in the challenge phenotype",
    },
    {
        "rank": 3,
        "name": "metformin",
        "research_analog": None,
        "label": "FDA AMPK activator; pediatric type 2 diabetes use",
        "axis": "AMPK / energy stress of aneuploidy (Tang 2011 Cell); milder mTORC1 brake",
        "child_match": "metabolic buffer, not a cytotoxic selector against mosaic cells",
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
]


def remaining_chain() -> dict:
    kept = STOP - 1
    return {
        "uniprot": UNIPROT,
        "stop": STOP,
        "kept_residues": kept,
        "lost_residues": 1050 - kept,
        "k668_remaining": K668 <= kept,
        "kinase_remaining": KINASE[0] <= kept,
        "n1002_in_kinase": KINASE[0] <= N1002 <= KINASE[1],
        "track1_cosic": {
            "eiip_fc_ratio_truncation": 0.810,
            "piezo_fc_ratio_truncation": 0.534,
            "note": "N-terminal resonance mostly intact; kinase-scale piezo harmonic halved",
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
        headers={"Content-Type": "application/json", "User-Agent": "genobank-track2/1"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.loads(r.read().decode())
    except Exception as e:
        return {"error": str(e)}


def main() -> None:
    out = {
        "disclaimer": "Research hypothesis. Not medical care. Genome gated.",
        "gene": "BUB1B",
        "disease": "Mosaic variegated aneuploidy syndrome 1",
        "remaining_chain": remaining_chain(),
        "candidates": CANDIDATES,
        "rejects": REJECTS,
        "opentargets": opentargets_bub1b(),
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
