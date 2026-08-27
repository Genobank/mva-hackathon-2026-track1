# MVA Hackathon 2026 (wisdom777 / GenoBank.io)

GenoBank.io BioFS submission for Rare Disease, Real Kid: The MVA Hackathon 2026.

Research hypothesis. Not medical care. Outputs CC BY 4.0. The genome is not in this repository.

Hugging Face account: `wisdom777`. Team name: GenoBank.io.

## Track 1 (submitted)

- `wisdom777_acmg-bub1b.csv` / `genobank_acmg-bub1b.csv`: predictions (PROBAND01, GRCh38)
- `wisdom777_track1_report.md`: methods
- `wisdom777_track1_methods.xlsx`: official judging form

Track 1 scored 100 / 100 rank points, F-max 1.000, full match at rank 1.

## Track 2 (drug repositioning)

- `genobank_track2_report.md`: mechanism plus 3 market-approved candidates
- `genobank_track2_methods.xlsx`: official judging form
- `track2/reposition_bub1b.py`: genome-free remaining-chain map
- `track2/pitch_script.txt` and `track2/genobank_track2_pitch.mp4`: 3-minute pitch (upload to YouTube or Vimeo before Space submit)

Candidates: nicotinamide (SIRT2/NAD+ stabilize remaining BUBR1 at K668), sirolimus (mTORC1 in BubR1 mice), metformin (AMPK). Mitotic poisons and aneuploid-cell killers are rejected as constitutional therapy.

## Ranking

1. Primary EPCR 0.92: BUB1B compound-het `chr15:40209701 T>G` (p.Leu737Ter, ClinVar 533901) plus `chr15:40220612 T>G` (p.Asn1002Lys, VUS, AM 0.9229, kinase)
2. Primary EPCR 0.90: BUB1B p.Leu737Ter alone (kinase 766 to 1050 deleted; piezo remaining-chain ratio 0.53)
3. Secondary EPCR 0.35: LZTR1 `chr22:20996720 C>G` (p.Tyr748Ter, ClinVar 1409252). Kelch and both BTB domains remain.

Independent VEP (ClawBio) and EVEE Evo 2 both call the two stop-gains pathogenic-class. EVEE names BUB1B p.Leu737Ter as Mosaic variegated aneuploidy syndrome 1. Cosic RRM is a mechanistic annotation, not a missense P/LP score.

## Reproduce the ranking (no genome in this repo)

The lab VCF is gated on Hugging Face (`SageBio/mva-hackathon-2026-data`) under WCG IRB 20252010. After access:

```
biofs onramp huggingface --repo SageBio/mva-hackathon-2026-data --owner <custodian> --serial EX2312012 --wait
biofs annotate submit EX2312012 --package rare_coding
biofs clinical EX2312012
biofs clawbio submit EX2312012 --wait
biofs rrm-consensus BUB1B --source orthologs
biofs psm-consensus BUB1B --source orthologs
biofs fourier-score 'BUB1B:p.Leu737Ter,BUB1B:p.Asn1002Lys' --encoding eiip --consensus-fc --null-model
biofs fourier-score 'BUB1B:p.Leu737Ter,BUB1B:p.Asn1002Lys' --encoding piezo --consensus-fc --null-model
```

`fourier-score` uses public UniProt sequences only. It does not read the genome.

CLI: `@genobank/biofs` 3.20.9. Node: biofs-node 0.4.23.
