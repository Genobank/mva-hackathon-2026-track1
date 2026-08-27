# Track 2: mechanism-matched drug repositioning for PROBAND01

GenoBank.io BioFS. Rare Disease, Real Kid MVA Hackathon 2026. Team GenoBank.io (Hugging Face wisdom777). Research hypothesis. Not medical care, diagnosis, or treatment. Outputs CC BY 4.0. The genome remains gated. No recontact.

This report starts from the Track 1 call: biallelic BUB1B loss of function (Mosaic variegated aneuploidy syndrome 1, OMIM 257300). It proposes 3 market-approved medicines whose mechanisms map onto that call, and it names the mitotic poisons, and the senolytic literature, that must not be repositioned as a constitutional therapy.

## Mechanism

PROBAND01 (serial EX2312012, GRCh38) carries two heterozygous BUB1B alleles on ENST00000287598.11 (UniProt O60566, 1050 residues):

1. chr15:40209701 T>G, c.2210T>G, p.Leu737Ter, **exon 17 of 23** (ClinVar 533901, Mosaic variegated aneuploidy syndrome 1).
2. chr15:40220612 T>G, c.3006T>G, p.Asn1002Lys (VUS, AlphaMissense 0.9229, kinase residue 1002, last exon).

Independent VEP and EVEE Evo 2 both treat the stop as pathogenic-class. EVEE names it Mosaic variegated aneuploidy syndrome 1. Phase is untested on a singleton. Biallelic BUB1B is the published architecture of MVA type 1 (one truncating allele plus one missense, or a hypomorphic second hit).

### What protein actually remains

p.Leu737Ter sits in exon 17 of 23. The last exon-exon junction is 6 exons downstream (exon 23 starts at chr15:40220564; the stop is at 40209701). A premature stop that far from the last exon-exon junction is NMD-expected on the 50-nucleotide rule. The default biochemical reading is therefore **not** a stable kinase-dead stub of residues 1 to 736. The default remaining BUBR1 protein is the full-length missense allele.

Two protein species are still on the map:

| Species | Source | Kinase | K668 (SIRT2 site) | How we treat it |
|---|---|---|---|---|
| Full-length p.Asn1002Lys | missense allele | present, residue 1002 altered | present | Default remaining protein. This is the North 2014 substrate class: hypomorphic full-length BUBR1. |
| Residues 1 to 736, if NMD-escape | stop allele | deleted (kinase 766 to 1050 is gone) | present | Escape product only. Cosic remaining-chain scores describe this polypeptide, not proof it is expressed. |

UniProt O60566:

- BUB1 N-terminal domain 62 to 226 (kinetochore / BUB3, GLEBS).
- Protein kinase 766 to 1050, active site 882.
- SIRT2 deacetylation site K668 (North et al., EMBO J 2014).

Cosic family-frequency scoring on the **escape polypeptide** 1 to 736: EIIP f_c 37.7 aa ratio 0.810 (N-terminal resonance mostly intact); piezo f_c 88.3 aa ratio 0.534 (kinase-scale dipole harmonic halved). That is the biochemical reading of a kinase-dead truncation that still encodes an N-terminal SAC adaptor. It is not a claim that NMD failed.

p.Asn1002Lys sits in the kinase, 10 residues from the published MVA missense L1012P (mouse L1002P in Sieben et al., JCI 2020). Fourier does not upgrade this VUS. AlphaMissense 0.9229 is the missense evidence.

BUBR1 (BUB1B) is a spindle-assembly-checkpoint kinase with kinase-independent kinetochore functions. Germline reduction of BUBR1 causes mosaic aneuploidy, growth failure, premature aging phenotypes, and cancer (Baker et al., Nat Genet 2004; Hanks et al.). There is no licensed disease-modifying drug for MVA (Malumbres, Nat Rev Genet 2024).

Challenge phenotype used as the clinical prior (not a return of results): rhabdomyosarcoma, nephrocalcinosis, short stature, failure to thrive, skeletal muscle atrophy, birth at 32 weeks, about 1 kg.

## What not to reposition

The Track 2 brief asks for market-approved medicines that target the disease-causing pathway. Several obvious mitosis drugs, and the most famous BubR1-mouse pharmacology, do the opposite of what this genotype needs as a constitutional therapy.

| Class | Examples | Why not |
|---|---|---|
| Microtubule poisons | vincristine, vinblastine, paclitaxel | Weaken attachment error-correction. Used in rhabdomyosarcoma protocols. They are not a constitutional MVA therapy. |
| Microtubule stabilizer (taxane-site class) | ivermectin | Human antiparasitic (Stromectol). Ashraf 2015/2016: binds the taxol pocket, promotes tubulin polymerization, reversible mitotic arrest. Freezes dynamics a weak SAC cannot police. Labeled Cmax is nanomolar; the tubulin effect is micromolar. |
| MPS1 / Aurora / CENP-E inhibitors | reversine, alisertib | Silence the checkpoint. BUBR1-low cells already have a weak SAC. |
| Aneuploid-cell killers | 17-AAG, high-dose AICAR (Tang and Amon, Cell 2011) | Select against aneuploid cells in culture. This child has constitutional mosaic aneuploidy. Killing mosaic cells is not a pediatric maintenance strategy. |
| Senolytics (BubR1H/H founding model) | dasatinib plus quercetin; INK-ATTAC clearance | Baker et al., Nature 2011 and 2016, cleared p16-positive senescent cells in BubR1-hypomorphic mice. D+Q is the clinical pair (Zhu et al., Aging Cell 2015). Not ranked: no pediatric MVA label; MVA plus rhabdomyosarcoma is a cancer-predisposition genome; senescent cells can be tumor-suppressive. |

Those agents remain relevant to tumour-directed care if a malignancy is treated on its own protocol. They are not Track 2 candidates for the germline SAC defect.

### Ivermectin, scored as a microtubule drug (not ranked)

Ivermectin is a licensed human medicine (FDA Stromectol for strongyloidiasis and onchocerciasis; pediatric mass-drug programmes exist, typically from 15 kg). The glutamate-gated chloride channel is the antiparasitic target. The microtubule claim is separate, and it is real enough to score.

Ashraf and Prichard showed direct tubulin binding. In *Haemonchus contortus*, ivermectin binds α- and β-tubulin at low micromolar affinity, overlaps the taxol site, and promotes polymerization (Int J Parasitol 2015; 45:647-654). In mammalian tubulin and HeLa cells it again increases polymer mass, protects microtubules from cold depolymerization, and reversibly stops cell division, taxol-like rather than vinca-like (Vet Parasitol 2016; 226:163-166). Avermectin B1a later reproduced polymerization promotion at 30 μM (Pharmaceuticals 2023; 16:1126). That is microtubule **stabilization**, not depolymerization. Error-correction at kinetochores needs microtubule turnover. Aurora B detaches incorrect fibers by promoting depolymerization. A taxane-class freeze suppresses that turnover. BUBR1 is in the mitotic checkpoint complex that would otherwise hold anaphase until attachments are fixed. This genome is BUBR1-low. The predicted cellular outcome is mitotic slippage with more lagging chromosomes, not a cleaner segregation.

Two dose facts close the constitutional-therapy reading. Stromectol 12 mg gives a mean Cmax of about 31 to 47 ng/mL, roughly 35 to 54 nM (Guzzo et al., J Clin Pharmacol 2002; Canga et al., AAPS J 2008). The published mammalian tubulin and HeLa effects sit at low micromolar concentrations, about 50 to 100 times that peak, and 93% plasma protein binding makes free drug smaller still. The labeled human dose does not reach the microtubule assay. A micromolar oncology experiment would still be a taxane-class insult to a weak SAC.

PAK1 degradation and Akt/mTOR inhibition (Dou et al.; Tang et al. reviews) are a second, extra-mitotic axis. That axis is already covered by sirolimus with a cleaner mTORC1 ligand. It cannot be isolated from the microtubule activity at the concentrations where PAK1 is hit.

R under the tubulin-stabilizer reading: M 0.25, G 0.10, P 0.15, L 0.85, C 0.55, **R = 14**. Under a PAK1/mTOR reading that still pays the microtubule penalty: **R = 24**. Either value sits below metformin and with the senolytics, not on the podium. Mebendazole, the human benzimidazole that actually inhibits tubulin polymerization at the colchicine site, scores the same way (**R = 13**). Human-approved is not the same as genotype-matched.

## Ranked candidates (market-approved)

All 3 are hypotheses. None is a recommendation to start a medicine. Evidence is mouse genetics plus human pediatric labelling, not an MVA trial.

### 1. Nicotinamide (niacinamide), with nicotinamide riboside as the research analog

**Label.** Nicotinamide is a licensed form of vitamin B3, used in children. Nicotinamide riboside (Niagen) and NMN are NAD+ precursors with human trials; they are not conventional prescription labels for a rare disease.

**Pathway.** CBP acetylates BUBR1 at K668 and primes the protein for ubiquitination. SIRT2, an NAD+-dependent deacetylase, removes that mark and stabilizes BUBR1. Raising NAD+ with NMN increases BUBR1 protein in mice. SIRT2 overexpression in BubR1-hypomorphic mice extends median lifespan 58% (North et al., EMBO J 2014; 33:1438-1453. doi:10.15252/embj.201386907).

**Why this child.** K668 is on the default remaining protein (full-length p.Asn1002Lys) and on any NMD-escape stub (668 < 737). North 2014 used hypomorphic **full-length** BUBR1. Under NMD, that mouse is the closer model, not a weaker one. A stabilizer of remaining BUBR1 is matched to a kinase-impaired missense plus a predicted-null stop. It does not restore the missing kinase active site. It can raise the abundance of the only BUBR1 this genome still makes.

**Limits.** Human NAD+ precursor trials are mixed and were not run in MVA. Nicotinamide at high dose can inhibit sirtuins (product inhibition), so the research analog NR/NMN is the closer North-2014 molecule. Any use is a clinical-trial question.

### 2. Metformin

**Label.** FDA-approved AMPK activator. Used in adolescents for type 2 diabetes and sometimes insulin resistance.

**Pathway.** Aneuploid cells are under energy and proteotoxic stress. Metformin and AICAR activate AMPK and impair accumulation of trisomic cells in culture (Tang et al., Cell 2011; 144:499-512). AMPK also inhibits mTORC1, so metformin sits on the same axis as sirolimus, milder.

**Why this child.** Failure to thrive and a constitutional mosaic-aneuploidy background. Metformin is the only AMPK drug with broad pediatric experience.

**The AICAR fork (same paper, opposite intent).** Tang and Amon scored aneuploid-cell killing. High-dose AICAR is on the reject list for that reason. Metformin is kept only as a metabolic buffer and a weak mTORC1 brake, not as a cytotoxic selector against this child's own mosaic cells. If a reader treats metformin as low-dose AICAR, it should move to the reject list with it.

**Limits.** Tang and Amon used AICAR more than metformin, and they were scoring cell competition, not a whole child. Gastrointestinal intolerance. Lactic acidosis risk in acute illness. No MVA trial.

### 3. Sirolimus (rapamycin)

**Label.** FDA-approved mTORC1 inhibitor. Pediatric use in tuberous sclerosis complex (SEGA, transplant, vascular anomalies). Everolimus is the close analog with pediatric oncology labels.

**Pathway.** Monoallelic BubR1 MVA-mimic mice show mTORC1 hyperactivity that tracks sarcopenia (Sieben et al., JCI 2020; 130:171. doi:10.1172/JCI126863). BubR1-insufficient mice develop muscle wasting and fat loss (Baker et al., 2004). Challenge phenotype includes skeletal muscle atrophy and failure to thrive. Rapamycin is the canonical mTORC1 drug.

**Why this child.** The published MVA mouse allelic series (X753 truncation without kinase; L1002P kinase missense) is the same architecture as p.Leu737Ter plus a kinase-domain missense **if** the stop allele produces protein. Under NMD, the closer mouse is BubR1 insufficiency plus a kinase missense. mTORC1 is downstream of BUBR1 insufficiency, not a SAC patch. The phenotypic match is growth, muscle, and aging-like tissue failure, not a claim that sirolimus restores chromosome segregation.

**Limits.** Immunosuppression, delayed wound healing, stomatitis, hyperlipidemia. A child with a rhabdomyosarcoma history needs oncology input before any mTOR inhibitor is even discussed. No MVA trial exists. This is a pathway hypothesis for the extra-mitotic, mTOR-linked phenotypes of BUBR1 loss.

## Thinking process (how the ranking was built)

1. Track 1 genotype: kinase-dead stop plus kinase missense, not a SAC-weakening missense in MAD2 or a microtubule-target mutation.
2. NMD: exon 17 of 23, so the default remaining protein is the full-length missense allele. Cosic remaining-chain scores describe the escape polypeptide, not proof of expression.
3. Remaining-protein geometry: K668 is on the missense protein for certain. Cosic EIIP 0.810 says an escape stub would still encode the N-terminal adaptor. Piezo 0.534 says the kinase harmonic would not. A kinase inhibitor has no intact substrate either way. A stabilizer does.
4. Fork. Restore remaining protein (SIRT2/NAD+). Brake extra-mitotic mTORC1 (sirolimus, metformin). Do not further silence mitosis. Do not run the BubR1 senolytic playbook on a cancer-predisposed child.
5. Phenotype overlay: muscle atrophy and failure to thrive raise mTOR/AMPK. Rhabdomyosarcoma history penalizes immunosuppression and senolytics.
6. Label overlay: Track 2 requires market-approved medicines. NR/NMN is the closer North-2014 molecule and is scored as a research analog, not as the labeled drug.

## Responsiveness index R (not a clinical probability)

R is a 0 to 100 index for this genotype, not a chance of benefit in a trial. Formula, weights fixed before scoring:

R = 100 × (0.35 M + 0.25 G + 0.20 P + 0.20 L) × (1 − C)

- M, mechanism identity. 1.00 acts on remaining BUBR1 protein. 0.60 published BubR1-mouse pathway, extra-mitotic. 0.40 metabolic analog of aneuploidy stress.
- G, geometry. 1.00 molecular site still on remaining protein (K668 on the missense allele; also on any escape stub). 0.50 extra-mitotic. 0.30 nonspecific.
- P, phenotype match to this HPO list (muscle atrophy, failure to thrive, short stature). 0 to 1.
- L, pediatric label. 1.00 licensed pediatric use. 0.70 vitamin with pediatric use. 0.40 research analog only.
- C, contraindication. 0.40 immunosuppression after rhabdomyosarcoma. 0.15 high-dose nicotinamide can inhibit sirtuins. 0 otherwise.

| Candidate | M | G | P | L | C | R |
|---|---|---|---|---|---|---|
| Nicotinamide (NR/NMN analog) | 1.00 | 1.00 | 0.40 | 0.70 | 0.15 | **70** |
| Metformin | 0.40 | 0.30 | 0.55 | 1.00 | 0.00 | **53** |
| Sirolimus | 0.60 | 0.50 | 0.85 | 1.00 | 0.40 | **42** |
| Senolytics D+Q (not ranked) | 0.65 | 0.20 | 0.45 | 0.30 | 0.55 | **19** |
| Ivermectin (not ranked) | 0.25 | 0.10 | 0.15 | 0.85 | 0.55 | **14** |

Worked nicotinamide: 0.35×1 + 0.25×1 + 0.20×0.40 + 0.20×0.70 = 0.82, then ×0.85 = 0.70. Sirolimus looks stronger on mouse mTORC1 until C = 0.40 for RMS-plus-immunosuppression. That is why it is third, not second.

### Sensitivity (rank order is not sacred)

Weights were frozen before scoring. The one weight that can reorder the podium is C on sirolimus, because the challenge document lists rhabdomyosarcoma and does not say whether that tumour is active.

| Case | Nicotinamide | Metformin | Sirolimus | Order |
|---|---|---|---|---|
| Base (C_sirolimus = 0.40) | 70 | 53 | 42 | NAM, MET, SIRO |
| No RMS penalty (C_sirolimus = 0) | 70 | 53 | **71** | NAM and SIRO essentially tied, then MET |
| Metformin treated as AICAR-class killer (moved to reject) | 70 | (reject) | 42 | NAM, SIRO |

The base ranking keeps the RMS penalty because the challenge phenotype includes rhabdomyosarcoma. A clinician who knew the tumour was remote could retie sirolimus with nicotinamide. R is not a posterior and is not calibrated on MVA outcomes. There are no MVA outcomes to calibrate on.

## Rank order and how to read it

1. Nicotinamide / NAD+ precursor. R = 70. Only ranked candidate whose molecular target is BUBR1 protein itself (K668 on the remaining missense protein).
2. Metformin. R = 53. Milder AMPK/mTOR lever, pediatric use, no RMS immunosuppression penalty. Kept only on the metabolic-buffer reading of Tang 2011, not the aneuploid-killer reading.
3. Sirolimus. R = 42. Strongest mTORC1 mouse match and strongest phenotype match, then the RMS penalty.

A research sequence, if a clinician ever opened an n-of-1 protocol, would start with the NAD+ precursor and keep mTOR inhibitors in an oncology-aware setting. That sequence is not a prescription.

## Secondary finding (not the MVA drug target)

LZTR1 p.Tyr748Ter is a real ClinVar pathogenic stop in a RASopathy / schwannomatosis gene. Remaining-chain Cosic f_c is preserved (Kelch and both BTB domains remain). It is not the MVA driver. MEK inhibitors used in severe Noonan syndrome are not proposed here. If RASopathy features were ever documented clinically, that would be a separate conversation, not this Track 2 ranking.

## Methods (judging form)

**Team name.** GenoBank.io (wisdom777).

**Approach.** Track 1 produced a kinase-dead BUB1B truncation plus a kinase missense. Track 2 first asks which protein remains (NMD on exon 17 of 23 via Ensembl REST on ENST00000287598; no FASTQ/BAM/VCF on the laptop), then maps that protein to 3 published axes: (1) SIRT2/NAD+ stabilization of BUBR1 at K668, (2) mTORC1 hyperactivity in BubR1 allelic-series mice, (3) AMPK as a milder metabolic/mTOR brake. Public literature (PubMed), UniProt domain map, Ensembl exon map, and the Cosic remaining-chain ratios are the inputs. OpenTargets/ChEMBL have no approved BUB1B-directed medicine; that negative result is recorded by `track2/reposition_bub1b.py` in the GitHub repository.

**Automation versus curation.** Domain mapping, exon lookup, and literature retrieval are scriptable. The reject list (mitotic poisons, aneuploid-cell killers, senolytics) and the 3-drug ranking were curated. The submission is not a raw database dump.

**Public data only.** Baker 2004 Nat Genet; Baker 2011 Nature; Baker 2016 Nature; Baker 2013 Nat Cell Biol; North 2014 EMBO J; Tang 2011 Cell; Zhu 2015 Aging Cell; Sieben 2020 JCI; Malumbres 2024 Nat Rev Genet; Ashraf 2015 Int J Parasitol; Ashraf 2016 Vet Parasitol; Guzzo 2002 J Clin Pharmacol; UniProt O60566; Ensembl ENST00000287598; ClinVar 533901; challenge HPO list. No proprietary compound library.

**Compound-het.** Track 1 already emits pairs. Track 2 treats both BUB1B alleles as one LoF genotype, with NMD making the missense allele the default remaining protein.

**Secondary findings.** LZTR1 is named and then left off the MVA drug list.

**Run time.** Literature, UniProt, and Ensembl exon mapping: hours on a laptop. No genome on the laptop. Cosic scores reused from Track 1 (biofs-node).

### Abstract (under 500 words)

MVA type 1 is biallelic BUB1B loss of function. This child has a stop in exon 17 of 23 (p.Leu737Ter) and a kinase missense (p.Asn1002Lys). A stop that far from the last exon is NMD-expected, so the default remaining protein is the full-length missense allele, not a kinase-dead stub. Cosic family-frequency scoring of the escape polypeptide still shows N-terminal SAC structure (EIIP ratio 0.810) and loss of the kinase-scale piezo harmonic (ratio 0.534). K668, the SIRT2 site that controls BUBR1 stability, is on the missense protein for certain.

No medicine is approved for MVA. Three market-approved agents map onto the published mouse genetics. Nicotinamide (with NR/NMN as the research NAD+ precursor) is the only ranked candidate that acts on BUBR1 protein abundance via SIRT2 (North 2014). Sirolimus addresses mTORC1 hyperactivity and sarcopenia in BubR1 allelic-series mice (Sieben 2020) and has a pediatric label. Metformin is a milder AMPK/mTOR lever with pediatric use, kept only as a metabolic buffer, not as the aneuploid-cell killer from the same Tang 2011 paper. Microtubule poisons, MPS1 inhibitors, aneuploid-cell killers, and BubR1-mouse senolytics are rejected as constitutional therapy.

A responsiveness index R (not a trial probability) ranks nicotinamide 70, metformin 53, sirolimus 42. Dropping the rhabdomyosarcoma immunosuppression penalty raises sirolimus to 71, essentially tied with nicotinamide. This is a research ranking for a judging panel. It is not a treatment plan.

## Scalability

The same map applies to CEP57 and TRIP13 MVA: ask which protein remains after NMD, score remaining-chain Cosic on any escape polypeptide, then SIRT2/NAD+ if a stability site remains, then mTOR/AMPK if extra-mitotic wasting is present, and keep senolytics off the constitutional list when cancer risk is part of the syndrome. The GitHub script is the public, genome-free half. Genomic bytes stay behind `biocid://` on biofs-node.

## Governance

No recontact. Delete underlying biodata within 30 days of programme close. Grant template `genobank:consent-template:genome-governance-ai-agent:v1`. Outputs CC BY 4.0. Genome gated.

Acknowledgement required by the Official Rules: this work was made possible through the Hackathon, organized by Sage Bionetworks in partnership with the MVA Society, Hugging Face, and BEACON, with prize sponsorship from AWS and Anthropic. We are deeply grateful to the child and their family who generously contributed their data and their story.

## Software and data

GenoBank.io BioFS CLI 3.20.9, biofs-node 0.4.23, Track 1 Cosic scores, UniProt O60566, Ensembl REST ENST00000287598 (exon 17 of 23), ClinVar, PubMed. Code: https://github.com/Genobank/mva-hackathon-2026-track1
