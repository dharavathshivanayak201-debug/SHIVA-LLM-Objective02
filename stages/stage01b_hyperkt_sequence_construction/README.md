# Stage 1B — HyperKT sequence construction (Objective 01, Stage 2)

**Notebook:** `HyperKT_Stage2_Sequence_Construction_FIXED.ipynb` · **Runtime:** Colab CPU · **Input:** `hyperkt_stage1.zip` · **Output archive:** `hyperkt_stage2.zip`

## Purpose
Builds the fixed-length training sequences consumed by the HyperKT model. Stage 2C later replays this exact construction to prove that every HyperKT prediction corresponds to one original ASSISTments event.

## Protocol
- Unknown skill = 0, padding = 1, vocabulary from 2 (preserved from Stage 1A).
- Targets 1…T−1 of each learner are split into **disjoint blocks of at most 200**; each target uses the immediately previous interaction as input, and causal attention is required in the model.
- Integrity checks: split overlap, label-shift correctness, no repeated target coverage, correct padding.
- Documented limitation: the first target of each block does not see the full preceding history.

## Recorded counts (`outputs/stage2_report.json`)
| Split | Students | Windows | Targets |
|---|---|---|---|
| Train | 3,330 | 3,706 | 222,562 |
| Validation | 416 | 445 | 23,858 |
| Test | 417 | 484 | 32,522 |

## Outputs
`train/val/test_sequences.npz` (padded history skill, history correctness, target skill, target correctness, mask), `stage2_report.json`, plus the copied `skill_vocab.json`, `train_cooccurrence.npz` and `manifest.json`.
