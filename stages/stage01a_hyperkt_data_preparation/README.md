# Stage 1A — HyperKT data preparation (Objective 01, Stage 1)

**Notebook:** `HyperKT_Stage1_ASSIST2009_Data_Preparation.ipynb` · **Runtime:** Colab CPU · **Output archive:** `hyperkt_stage1.zip`

## Purpose
Reproduces the Objective 01 (HyperKT) preprocessing that defines the learner partitions and skill vocabulary used by the frozen HyperKT model. Objective 02 depends on these exact artefacts to recover event-level alignment in Stage 2C.

## Method
1. Reads the raw CSV and records its **SHA-256** (`162ef8d2…a6e5da`).
2. Maps columns `user_id`, `skill_id`, `correct`, `order_id`; drops missing values; refuses to proceed if multi-skill rows (`~~` or `,`) are present.
3. Stable sort by learner → `order_id` → original row position.
4. **Student-disjoint 80/10/10 split** (seed 42), made **before** fitting any vocabulary.
5. Skill vocabulary from training learners only (ID 0 = unknown, ID 1 = padding, real skills from 2).
6. Train-only skill co-occurrence matrix over sliding windows of 5 interactions (sparse, normalised).

## Recorded data facts (`outputs/manifest.json`)
| Item | Value |
|---|---|
| Raw rows | 346,860 |
| Clean rows | 283,105 |
| Students | 4,163 |
| Skills (all / train) | 149 / 149 |
| Co-occurrence windows | 225,892 |

## Outputs
| File | Description |
|---|---|
| `train/val/test_interactions.parquet` | Split interaction tables with mapped `skill_id` |
| `skill_vocab.json` | Training-only skill → integer ID map |
| `train_cooccurrence.npz` | Sparse train-only skill co-occurrence matrix |
| `manifest.json` | Seed, source checksum, row counts, split rule and exact split learner IDs |
