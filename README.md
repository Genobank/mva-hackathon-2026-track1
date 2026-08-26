# MVA Hackathon 2026 Track 1 (wisdom777)

GenoBank.io BioFS submission for Rare Disease, Real Kid: The MVA Hackathon 2026, Track 1 (variant prediction).

Research hypothesis. Not medical care. Outputs CC BY 4.0. The genome is not in this repository.

Hugging Face account: `wisdom777`

## Files

- `wisdom777_acmg-bub1b.csv` — Track 1 predictions (PROBAND01, GRCh38)
- `wisdom777_track1_report.md` — methods

## Ranking

1. Primary EPCR 0.92: BUB1B compound-het `chr15:40209701 T>G` (p.Leu737Ter, ClinVar 533901) plus `chr15:40220612 T>G` (p.Asn1002Lys, VUS)
2. Primary EPCR 0.88: BUB1B p.Leu737Ter alone
3. Secondary EPCR 0.35: LZTR1 `chr22:20996720 C>G` (p.Tyr748Ter, ClinVar 1409252)

Independent VEP (ClawBio) and EVEE Evo 2 both call the two stop-gains pathogenic-class. EVEE names BUB1B p.Leu737Ter as Mosaic variegated aneuploidy syndrome 1.

## Reproduce the ranking (no genome in this repo)

The lab VCF is gated on Hugging Face (`SageBio/mva-hackathon-2026-data`) under WCG IRB 20252010. After access:

```
biofs onramp huggingface --repo SageBio/mva-hackathon-2026-data --owner <custodian> --serial EX2312012 --wait
biofs annotate submit EX2312012 --package rare_coding
biofs clinical EX2312012
biofs clawbio submit EX2312012 --wait
```

CLI: `@genobank/biofs` 3.20.7. Node: biofs-node 0.4.22.
