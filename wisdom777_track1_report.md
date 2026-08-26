# Track 1 methods: PROBAND01 (wisdom777)

GenoBank.io BioFS rare-disease variant prioritization for the 2026 Rare Disease, Real Kid MVA hackathon. Research hypothesis. Not medical care, diagnosis, or treatment. Outputs CC BY 4.0. The genome remains gated.

## Data

Biosample serial EX2312012. Scoring id PROBAND01. Assembly GRCh38 (hg38). Singleton Illumina WGS, 4 paired FASTQ lanes, plus the lab VCF `WGS_EX2312012_HGWCNDSX7.vcf.gz`.

Files were on-ramped server-side (`biofs onramp huggingface`) into BioRouter under a claimable family custodian biowallet. 11 objects registered. Genomic bytes did not land on a laptop. Address is `biocid://` only.

This ranking is scored from the lab VCF. A Clara Parabricks germline DeepVariant job on the 4 lane pairs was submitted and is not part of this model.

## Pipeline

1. OpenCRAVAT package `rare_coding`, assembly hg38, job `oc-a76b7172-0ec6-4ab5-98f4-b3c5c43aa711`. 4740790 PASS variants.
2. `biofs clinical` ACMG/AMP 2015 + ClinGen-SVI 2024, gnomAD AF ceiling 0.01. 10613 variants classified: Pathogenic 1 (LZTR1 p.Tyr748Ter), Likely Pathogenic 1 (BUB1B p.Leu737Ter), VUS 10610, Likely Benign 1.
3. Independent consensus on biofs-node (`biofs clawbio submit`, job `cb-77eb64be-3275-41ba-8c7a-f8155dfc6a8c`): ClawBio-compatible Ensembl VEP REST GRCh38 (Tier 1–4) and EVEE Evo 2 (Pearce et al. 2026). Candidate alleles only; the genome was not sent to either service.

The rare-coding set contains exactly 2 stop-gains: BUB1B p.Leu737Ter and LZTR1 p.Tyr748Ter.

## Independent concordance

| Allele | ACMG | ClawBio VEP | EVEE Evo 2 |
|---|---|---|---|
| BUB1B p.Leu737Ter | Likely pathogenic; ClinVar 533901; Mosaic variegated aneuploidy syndrome 1 | Tier 1, score 157, stop-gain | Pathogenic 0.9681; disease Mosaic variegated aneuploidy syndrome 1 |
| BUB1B p.Asn1002Lys | VUS missense; no ClinVar | Tier 2, score 73, missense | Not in the 4.2 million ClinVar index |
| LZTR1 p.Tyr748Ter | Pathogenic; ClinVar 1409252 | Tier 1, score 157, stop-gain | Pathogenic 0.9706; LoEUF unconstrained |

MAD1L1 missense was a ClawBio Tier 1 false lead (mixed ClinVar strings). EVEE calls it Benign (0.4904). It is not in the prediction file.

## Ranked calls

1. Primary, EPCR 0.92. BUB1B compound-het on GRCh38: chr15:40209701 T>G (c.2210T>G p.Leu737Ter, ClinVar 533901) plus chr15:40220612 T>G (c.3006T>G p.Asn1002Lys, VUS). Both heterozygous. Phase untested on a singleton. Biallelic BUB1B is Mosaic variegated aneuploidy syndrome 1 (OMIM 257300).
2. Primary, EPCR 0.88. The same BUB1B p.Leu737Ter allele alone, if the scorer treats a single reported MVA1 variant as sufficient.
3. Secondary, EPCR 0.35. LZTR1 chr22:20996720 C>G (c.2244C>G p.Tyr748Ter, ClinVar 1409252). Pathogenic in a RASopathy / schwannomatosis gene. Not submitted as the MVA driver.

## Governance

No recontact. Delete underlying biodata within 30 days of programme close (`biofs erase`). Grant template `genobank:consent-template:genome-governance-ai-agent:v1`, BioPIL 5, purpose code 1001 research.

## Software

GenoBank.io BioFS CLI 3.20.7, biofs-node 0.4.22, OpenCRAVAT rare_coding, biofs clinical ACMG/AMP 2015 + ClinGen-SVI 2024, ClawBio variant-annotation 0.3.0 compatible VEP REST, EVEE Evo 2. Hugging Face account wisdom777.
