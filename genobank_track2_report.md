# Track 2: mechanism-matched drug repositioning for PROBAND01

GenoBank.io BioFS. Rare Disease, Real Kid MVA Hackathon 2026. Team GenoBank.io (Hugging Face wisdom777). Research hypothesis. Not medical care, diagnosis, or treatment. Outputs CC BY 4.0. The genome remains gated. No recontact.

This report starts from the Track 1 call: biallelic BUB1B loss of function (Mosaic variegated aneuploidy syndrome 1, OMIM 257300). It proposes 3 market-approved medicines whose mechanisms map onto that call, and it names the mitotic poisons that must not be repositioned as a constitutional therapy.

## Mechanism

PROBAND01 (serial EX2312012, GRCh38) carries two heterozygous BUB1B alleles:

1. chr15:40209701 T>G, c.2210T>G, p.Leu737Ter (ClinVar 533901, Mosaic variegated aneuploidy syndrome 1).
2. chr15:40220612 T>G, c.3006T>G, p.Asn1002Lys (VUS, AlphaMissense 0.9229, kinase residue 1002).

Independent VEP and EVEE Evo 2 both treat the stop as pathogenic-class. EVEE names it Mosaic variegated aneuploidy syndrome 1. Phase is untested on a singleton. Biallelic BUB1B is the published architecture of MVA type 1 (one truncating allele plus one missense, or a hypomorphic second hit).

UniProt O60566 (1050 residues):

- BUB1 N-terminal domain 62 to 226 (kinetochore / BUB3, GLEBS).
- Protein kinase 766 to 1050, active site 882.
- SIRT2 deacetylation site K668 (North et al., EMBO J 2014).

p.Leu737Ter keeps residues 1 to 736. The kinase is gone. K668 remains. Cosic family-frequency scoring on the remaining chain: EIIP f_c 37.7 aa ratio 0.810 (N-terminal resonance mostly intact); piezo f_c 88.3 aa ratio 0.534 (kinase-scale dipole harmonic halved). That is the biochemical reading of a kinase-dead truncation that still presents an N-terminal SAC adaptor.

p.Asn1002Lys sits in the kinase, 10 residues from the published MVA missense L1012P (mouse L1002P in Sieben et al., JCI 2020). Fourier does not upgrade this VUS. AlphaMissense 0.9229 is the missense evidence.

BUBR1 (BUB1B) is a spindle-assembly-checkpoint kinase with kinase-independent kinetochore functions. Germline reduction of BUBR1 causes mosaic aneuploidy, growth failure, premature aging phenotypes, and cancer (Baker et al., Nat Genet 2004; Hanks et al.). There is no licensed disease-modifying drug for MVA (Malumbres, Nat Rev Genet 2024).

Challenge phenotype used as the clinical prior (not a return of results): rhabdomyosarcoma, nephrocalcinosis, short stature, failure to thrive, skeletal muscle atrophy, birth at 32 weeks, about 1 kg.

## What not to reposition

The Track 2 brief asks for market-approved medicines that target the disease-causing pathway. Several obvious mitosis drugs do the opposite of what this genotype needs.

| Class | Examples | Why not |
|---|---|---|
| Microtubule poisons | vincristine, vinblastine, paclitaxel | Weaken attachment error-correction. Used in rhabdomyosarcoma protocols. They are not a constitutional MVA therapy. |
| MPS1 / Aurora / CENP-E inhibitors | reversine, alisertib | Silence the checkpoint. BUBR1-low cells already have a weak SAC. |
| Aneuploid-cell killers | 17-AAG, high-dose AICAR (Tang and Amon, Cell 2011) | Select against aneuploid cells in culture. This child has constitutional mosaic aneuploidy. Killing mosaic cells is not a pediatric maintenance strategy. |

Those agents remain relevant to tumour-directed care if a malignancy is treated on its own protocol. They are not Track 2 candidates for the germline SAC defect.

## Ranked candidates (market-approved)

All 3 are hypotheses. None is a recommendation to start a medicine. Evidence is mouse genetics plus human pediatric labelling, not an MVA trial.

### 1. Nicotinamide (niacinamide), with nicotinamide riboside as the research analog

**Label.** Nicotinamide is a licensed form of vitamin B3, used in children. Nicotinamide riboside (Niagen) and NMN are NAD+ precursors with human trials; they are not conventional prescription labels for a rare disease.

**Pathway.** CBP acetylates BUBR1 at K668 and primes the protein for ubiquitination. SIRT2, an NAD+-dependent deacetylase, removes that mark and stabilizes BUBR1. Raising NAD+ with NMN increases BUBR1 protein in mice. SIRT2 overexpression in BubR1-hypomorphic mice extends median lifespan 58% (North et al., EMBO J 2014; 33:1438-1453. doi:10.15252/embj.201386907).

**Why this child.** K668 is residue 668. The stop at 737 leaves K668 on the truncated chain. The missense allele is full-length and also carries K668. A stabilizer of remaining BUBR1 protein is matched to a kinase-dead truncation plus a kinase missense. It does not restore the missing kinase active site. It can raise the abundance of the N-terminal adaptor that Cosic EIIP still sees (ratio 0.810).

**Limits.** Human NAD+ precursor trials are mixed and were not run in MVA. Mouse data used hypomorphic full-length protein, not an allele that ends at 737. Nicotinamide at high dose can inhibit sirtuins (product inhibition), so the research analog NR/NMN is the closer North-2014 molecule. Any use is a clinical-trial question.

### 2. Sirolimus (rapamycin)

**Label.** FDA-approved mTORC1 inhibitor. Pediatric use in tuberous sclerosis complex (SEGA, transplant, vascular anomalies). Everolimus is the close analog with pediatric oncology labels.

**Pathway.** Monoallelic BubR1 MVA-mimic mice show mTORC1 hyperactivity that tracks sarcopenia (Sieben et al., JCI 2020; 130:171. doi:10.1172/JCI126863). BubR1-insufficient mice develop muscle wasting and fat loss (Baker et al., 2004). Challenge phenotype includes skeletal muscle atrophy and failure to thrive. Rapamycin is the canonical mTORC1 drug.

**Why this child.** The published MVA mouse allelic series (X753 truncation without kinase; L1002P kinase missense) is the same architecture as p.Leu737Ter plus a kinase-domain missense. mTORC1 is downstream of BUBR1 insufficiency, not a SAC patch. The phenotypic match is growth, muscle, and aging-like tissue failure, not a claim that sirolimus restores chromosome segregation.

**Limits.** Immunosuppression, delayed wound healing, stomatitis, hyperlipidemia. A child with a rhabdomyosarcoma history needs oncology input before any mTOR inhibitor is even discussed. No MVA trial exists. This is a pathway hypothesis for the extra-mitotic, mTOR-linked phenotypes of BUBR1 loss.

### 3. Metformin

**Label.** FDA-approved AMPK activator. Used in adolescents for type 2 diabetes and sometimes insulin resistance.

**Pathway.** Aneuploid cells are under energy and proteotoxic stress. Metformin and AICAR activate AMPK and impair accumulation of trisomic cells in culture (Tang et al., Cell 2011; 144:499-512). AMPK also inhibits mTORC1, so metformin sits on the same axis as sirolimus, milder.

**Why this child.** Failure to thrive and a constitutional mosaic-aneuploidy background. Metformin is the only AMPK drug with broad pediatric experience. It is not framed here as a cytotoxic selector against the child's own mosaic cells. It is framed as a metabolic buffer and a weak mTORC1 brake.

**Limits.** Tang and Amon used AICAR more than metformin, and they were scoring cell competition, not a whole child. Gastrointestinal intolerance. Lactic acidosis risk in acute illness. No MVA trial.

## Rank order and how to read it

1. Nicotinamide / NAD+ precursor: the only candidate whose molecular target is BUBR1 protein itself (K668 on the remaining chain).
2. Sirolimus: strongest approved drug for the mTORC1-linked extra-mitotic phenotypes in BubR1 mice, highest monitoring burden.
3. Metformin: lowest-intensity AMPK/mTOR lever with pediatric use.

A sensible research sequence, if a clinician ever opened an n-of-1 protocol, would start with the NAD+ precursor (closest to BUBR1 abundance) and keep mTOR inhibitors in a monitored oncology-aware setting. That sequence is not a prescription.

## Secondary finding (not the MVA drug target)

LZTR1 p.Tyr748Ter is a real ClinVar pathogenic stop in a RASopathy / schwannomatosis gene. Remaining-chain Cosic f_c is preserved (Kelch and both BTB domains remain). It is not the MVA driver. MEK inhibitors used in severe Noonan syndrome are not proposed here. If RASopathy features were ever documented clinically, that would be a separate conversation, not this Track 2 ranking.

## Methods (judging form)

**Team name.** GenoBank.io (wisdom777).

**Approach.** Track 1 produced a kinase-dead BUB1B truncation plus a kinase missense. Track 2 maps that protein to 3 published axes: (1) SIRT2/NAD+ stabilization of BUBR1 at K668, (2) mTORC1 hyperactivity in BubR1 allelic-series mice, (3) AMPK as a milder metabolic/mTOR brake. Public literature (PubMed), UniProt domain map, and the Cosic remaining-chain ratios are the inputs. OpenTargets/ChEMBL have no approved BUB1B-directed medicine; that negative result is recorded by `track2/reposition_bub1b.py` in the GitHub repository.

**Automation versus curation.** Domain mapping and literature retrieval are scriptable. The reject list (mitotic poisons, aneuploid-cell killers) and the 3-drug ranking were curated. The submission is not a raw database dump.

**Public data only.** Baker 2004 Nat Genet; Baker 2013 Nat Cell Biol; North 2014 EMBO J; Tang 2011 Cell; Sieben 2020 JCI; Malumbres 2024 Nat Rev Genet; UniProt O60566; ClinVar 533901; challenge HPO list. No proprietary compound library.

**Compound-het.** Track 1 already emits pairs. Track 2 treats both BUB1B alleles as one LoF genotype.

**Secondary findings.** LZTR1 is named and then left off the MVA drug list.

**Run time.** Literature and UniProt mapping: hours on a laptop. No genome on the laptop. Cosic scores reused from Track 1 (biofs-node).

### Abstract (under 500 words)

MVA type 1 is biallelic BUB1B loss of function. This child has a kinase-deleting stop (p.Leu737Ter) and a kinase missense (p.Asn1002Lys). Cosic family-frequency scoring shows the remaining chain still carries N-terminal SAC structure (EIIP ratio 0.810) while the kinase-scale piezo harmonic is lost (ratio 0.534). K668, the SIRT2 site that controls BUBR1 stability, is on the remaining chain.

No medicine is approved for MVA. Three market-approved agents map onto the published mouse genetics. Nicotinamide (with NR/NMN as the research NAD+ precursor) is the only one that acts on BUBR1 protein abundance via SIRT2 (North 2014). Sirolimus addresses mTORC1 hyperactivity and sarcopenia in BubR1 allelic-series mice (Sieben 2020) and has a pediatric label. Metformin is a milder AMPK/mTOR lever with pediatric use. Microtubule poisons, MPS1 inhibitors, and aneuploid-cell killers are rejected as constitutional therapy: they worsen a weak checkpoint or select against mosaic cells that are the child's tissues.

This is a research ranking for a judging panel. It is not a treatment plan.

## Scalability

The same map applies to CEP57 and TRIP13 MVA: remaining-chain Cosic on the LoF allele, then SIRT2/NAD+ if a stability site remains, then mTOR/AMPK if extra-mitotic wasting is present. The GitHub script is the public, genome-free half. Genomic bytes stay behind `biocid://` on biofs-node.

## Governance

No recontact. Delete underlying biodata within 30 days of programme close. Grant template `genobank:consent-template:genome-governance-ai-agent:v1`. Outputs CC BY 4.0. Genome gated.

Acknowledgement required by the Official Rules: this work was made possible through the Hackathon, organized by Sage Bionetworks in partnership with the MVA Society, Hugging Face, and BEACON, with prize sponsorship from AWS and Anthropic. We are deeply grateful to the child and their family who generously contributed their data and their story.

## Software and data

GenoBank.io BioFS CLI 3.20.9, biofs-node 0.4.23, Track 1 Cosic scores, UniProt O60566, ClinVar, PubMed. Code: https://github.com/Genobank/mva-hackathon-2026-track1
