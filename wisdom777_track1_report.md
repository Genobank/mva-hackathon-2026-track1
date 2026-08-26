# Track 1 methods: PROBAND01 (wisdom777)

GenoBank.io BioFS rare-disease variant prioritization for the 2026 Rare Disease, Real Kid MVA hackathon. Research hypothesis. Not medical care, diagnosis, or treatment. Outputs CC BY 4.0. The genome remains gated.

## Data

Biosample serial EX2312012. Scoring id PROBAND01. Assembly GRCh38 (hg38). Singleton Illumina WGS, 4 paired FASTQ lanes, plus the lab VCF `WGS_EX2312012_HGWCNDSX7.vcf.gz`.

Files were on-ramped server-side (`biofs onramp huggingface`) into BioRouter under a claimable family custodian biowallet. 11 objects registered. Genomic bytes did not land on a laptop. Address is `biocid://` only.

This ranking is scored from the lab VCF. A Clara Parabricks germline DeepVariant job on the 4 lane pairs was submitted and is not part of this model.

## Pipeline

1. OpenCRAVAT package `rare_coding`, assembly hg38, job `oc-a76b7172-0ec6-4ab5-98f4-b3c5c43aa711`. 4740790 PASS variants.
2. `biofs clinical` ACMG/AMP 2015 + ClinGen-SVI 2024, gnomAD AF ceiling 0.01. 10613 variants classified: Pathogenic 1 (LZTR1 p.Tyr748Ter), Likely Pathogenic 1 (BUB1B p.Leu737Ter), VUS 10610, Likely Benign 1.
3. Independent consensus on biofs-node (`biofs clawbio submit`, job `cb-77eb64be-3275-41ba-8c7a-f8155dfc6a8c`): ClawBio-compatible Ensembl VEP REST GRCh38 (Tier 1 to 4) and EVEE Evo 2 (Pearce et al. 2026). Candidate alleles only; the genome was not sent to either service.
4. Cosic RRM on family characteristic frequency (`biofs rrm-consensus`, `biofs psm-consensus`, `biofs fourier-score --encoding eiip|piezo --null-model`). Validated on ClinVar GRCh38, 356 genes, 55971 AlphaMissense hits, 66335 pathogenic truncations (biofs-node job `cw-dfdb9a9b-9d83-4c6f-a461-db0aaa218855`).

The rare-coding set contains exactly 2 stop-gains: BUB1B p.Leu737Ter and LZTR1 p.Tyr748Ter.

## Independent concordance

| Allele | ACMG | ClawBio VEP | EVEE Evo 2 |
|---|---|---|---|
| BUB1B p.Leu737Ter | Likely pathogenic; ClinVar 533901; Mosaic variegated aneuploidy syndrome 1 | Tier 1, score 157, stop-gain | Pathogenic 0.9681; disease Mosaic variegated aneuploidy syndrome 1 |
| BUB1B p.Asn1002Lys | VUS missense; no ClinVar | Tier 2, score 73, missense | Not in the 4.2 million ClinVar index |
| LZTR1 p.Tyr748Ter | Pathogenic; ClinVar 1409252 | Tier 1, score 157, stop-gain | Pathogenic 0.9706; LoEUF unconstrained |

MAD1L1 missense was a ClawBio Tier 1 false lead (mixed ClinVar strings). EVEE calls it Benign (0.4904). It is not in the prediction file.

## Wave analysis (family f_c, EIIP + piezo)

Missense Fourier is not used as a P/LP score. On 356 ClinVar genes the best wave feature (`piezo_win_df`) has mean AUC 0.58 versus AlphaMissense 0.95 (0 of 356 genes Fourier > AM). Truncation remaining-chain |X(f_c)| is the wave LoF metric: 97.4% of 66335 ClinVar P/LP stops have ratio <0.9, median 0.41.

BUB1B family EIIP f_c is 37.7 aa (40 vertebrate orthologs, functional band 8 to 80 aa). BUB1B family piezo f_c is 88.3 aa (100 orthologs, 23 sigma, domain scale). UniProt O60566: BUB1 N-terminal 62 to 226, protein kinase 766 to 1050, active site 882.

| Allele | Encoding | Family period | Call | Remaining or native ratio | Domain |
|---|---|---|---|---|---|
| BUB1B p.Leu737Ter | EIIP | 37.7 aa | mild f_c loss | 0.810 | Remaining chain 1 to 736; kinase gone |
| BUB1B p.Leu737Ter | piezo | 88.3 aa | disrupts f_c | 0.534 | Kinase-scale dipole harmonic halved |
| BUB1B p.Asn1002Lys | EIIP | 37.7 aa | weakly destructive | 0.992 | Asn is EIIP-silent; null dest 47th pctl |
| BUB1B p.Asn1002Lys | piezo | 88.3 aa | constructive | 1.014 | In kinase; local dipole loud, family harmonic not opposed |
| LZTR1 p.Tyr748Ter | EIIP | 50.7 aa | preserves f_c | 0.952 | Kelch 1 to 6 and both BTB domains remain |
| MAD1L1 p.Arg59Cys | EIIP | 3.45 aa helix | not used |  | Coiled-coil helical artifact; ClinVar benign |

The stop is the wave-positive event for this child. Removing 314 residues deletes the kinase and drops the 88 aa piezo harmonic to 53% of wild type, inside the ClinVar pathogenic truncation band. The N-terminal BUB1 domain still carries most of the EIIP 37.7 aa resonance (ratio 0.81), which is why EIIP alone looked only mild.

p.Asn1002Lys sits in the kinase (residue 1002). AlphaMissense 0.9229 is the missense evidence. Fourier does not upgrade it: EIIP cannot see Asn, and piezo does not oppose the family harmonic. The compound-het hypothesis remains AR MVA1 biology (two BUB1B hits) plus that AM score, not a Cosic P/LP conversion.

LZTR1 p.Tyr748Ter is a real pathogenic stop in a RASopathy gene. Remaining-chain f_c is preserved because Kelch and both BTB domains (443 to 537 and 667 to 736) stay. It is not submitted as the MVA driver.

## Ranked calls

1. Primary, EPCR 0.92. BUB1B compound-het on GRCh38: chr15:40209701 T>G (c.2210T>G p.Leu737Ter, ClinVar 533901) plus chr15:40220612 T>G (c.3006T>G p.Asn1002Lys, VUS, AM 0.9229, kinase). Both heterozygous. Phase untested on a singleton. Biallelic BUB1B is Mosaic variegated aneuploidy syndrome 1 (OMIM 257300).
2. Primary, EPCR 0.90. The same BUB1B p.Leu737Ter allele alone: kinase 766 to 1050 deleted, piezo remaining-chain ratio 0.53. Use if the scorer treats a single reported MVA1 variant as sufficient.
3. Secondary, EPCR 0.35. LZTR1 chr22:20996720 C>G (c.2244C>G p.Tyr748Ter, ClinVar 1409252). Pathogenic in a RASopathy / schwannomatosis gene. Family f_c preserved. Not the MVA driver.

## Methods description (judging)

Team name: GenoBank.io. Hugging Face account: wisdom777. Model 1 of 6.

The allele-calling stack is automated: OpenCRAVAT `rare_coding`, ACMG/AMP 2015 + ClinGen-SVI 2024 (Pejaver-2022 PP3/BP4), Ensembl VEP REST (ClawBio-compatible), EVEE Evo 2, and Cosic RRM (EIIP and side-chain dipole) on family characteristic frequency. Genomic bytes stay on biofs-node. The 3-row CSV is not a raw dump of 10613 ACMG classes. Compound-het pairing and EPCR values were assigned after those outputs. The allele list was not hand-searched beyond the rare-coding stop-gains (exactly 2) plus the BUB1B kinase missense that AlphaMissense scored 0.9229.

Public data only. ClinVar (including GRCh38 allele VCF, stars ≥ 1, 356-gene missense hold-out and 66335 pathogenic truncations), gnomAD, UniProt Swiss-Prot/TrEMBL orthologs, AlphaMissense, REVEL, CADD, SpliceAI, Ensembl VEP, EVEE/Evo 2 ClinVar catalog. The genome is the challenge dataset (`SageBio/mva-hackathon-2026-data`, WCG IRB 20252010). No proprietary variant database.

The approach emits compound-het pairs (row 1) and single-variant rows (rows 2 and 3). Secondary finding: LZTR1 p.Tyr748Ter, a real ClinVar pathogenic stop in a RASopathy gene whose remaining-chain family f_c is preserved. `finding_type=secondary` so it does not compete as the MVA driver. Secondary rows do not reduce rank points; F-max is swept on EPCR thresholds, so the 0.92 compound-het row can still score F=1 if that pair is gold.

Run time on the existing GenoBank.io production node: OpenCRAVAT rare_coding on 4740790 PASS variants; ACMG on 10613; ClawBio+EVEE 16 candidate alleles in 32 seconds; ClinVar wave job on 356 genes. The laptop only orchestrates. No extra cloud bill was opened for this case.

### Abstract

Mosaic variegated aneuploidy is a spindle-checkpoint disease. On this singleton GRCh38 WGS the rare-coding set contains 2 stop-gains: BUB1B p.Leu737Ter (ClinVar 533901, MVA1) and LZTR1 p.Tyr748Ter (ClinVar 1409252, RASopathy/schwannomatosis). Independent VEP and EVEE both call those stops pathogenic-class. EVEE names the BUB1B allele Mosaic variegated aneuploidy syndrome 1. Biallelic BUB1B is OMIM 257300, so the ranking pairs the stop with the only rare BUB1B missense that is strong on AlphaMissense (p.Asn1002Lys, 0.9229, kinase residue 1002). Phase is untested.

Cosic RRM is used as a mechanistic annotation, not as a missense P/LP probability. On 356 ClinVar genes the best wave feature has mean AUC 0.58 versus AlphaMissense 0.95. Truncation remaining-chain |X(f_c)| is the wave LoF metric (97.4% of 66335 P/LP stops < 0.9, median 0.41). For p.Leu737Ter, EIIP family f_c (37.7 aa) stays at 0.81 because the N-terminal BUB1 domain remains; piezo family f_c (88.3 aa) falls to 0.53 because UniProt kinase 766 to 1050 is deleted. p.Asn1002Lys is not upgraded by Fourier. LZTR1 keeps Kelch and both BTB domains; family f_c is preserved, so it is secondary.

Strengths: protocol-gated WGS (no genome on a laptop), two independent public annotators, domain-aware wave LoF on the stop, honest missense limits, compound-het row in the scorer's native shape. Limits: singleton so phase is unknown; Clara DeepVariant was submitted and is not in this model; missense Fourier is not calibrated as pathogenicity; EPCR is assigned, not a posterior from a trained head.

## Governance

No recontact. Delete underlying biodata within 30 days of programme close (`biofs erase`). Grant template `genobank:consent-template:genome-governance-ai-agent:v1`, BioPIL 5, purpose code 1001 research.

## Software

GenoBank.io BioFS CLI 3.20.9, biofs-node 0.4.23, OpenCRAVAT rare_coding, biofs clinical ACMG/AMP 2015 + ClinGen-SVI 2024 (Pejaver-2022 PP3/BP4), ClawBio variant-annotation 0.3.0 compatible VEP REST, EVEE Evo 2, Cosic RRM (`rrm_fft.py`) with EIIP and side-chain dipole (Avbelj 2000 / Cieplak 2009). Hugging Face account wisdom777.
