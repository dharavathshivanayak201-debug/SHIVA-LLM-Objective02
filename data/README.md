# Data

## `skill_builder_data_corrected_collapsed.csv.gz`
The ASSISTments 2009–2010 Skill Builder dataset (corrected, collapsed version) used by every stage. It is gzip-compressed here; read it with `pd.read_csv('data/skill_builder_data_corrected_collapsed.csv.gz', encoding='latin-1', low_memory=False)` or decompress with `gunzip -k`.

| Property | Value |
|---|---|
| SHA-256 of the uncompressed CSV | `162ef8d2d28bcbfea6591a282994062bd8d5eaa00636544292a0d268dca6e5da` |
| Raw rows | 346,860 |
| Rows after cleaning (Stage 1A) | 283,105 |
| Students | 4,163 |
| Skills | 149 |
| Columns used | `user_id`, `skill_id`, `problem_id`, `correct`, `order_id` |

The Stage 1A notebook records the same SHA-256 in `stages/stage01a_hyperkt_data_preparation/outputs/manifest.json`, so you can verify the file:

```bash
gunzip -c data/skill_builder_data_corrected_collapsed.csv.gz | sha256sum
```

## Source and terms
The dataset is published by the ASSISTments project for research use. Learner IDs are anonymised identifiers assigned by ASSISTments. When using it, cite:

> Feng, M., Heffernan, N. T., & Koedinger, K. R. (2009). Addressing the assessment challenge with an online system that tutors as it assesses. *User Modeling and User-Adapted Interaction*, 19(3), 243–266.

Please also follow the ASSISTments data-use terms on the official ASSISTments dataset pages. This repository does not relicense the data; see [../RIGHTS.md](../RIGHTS.md).

## Derived data
All derived datasets (HyperKT predictions, event crosswalk, aligned reward/transition tables, response-model predictions) are in each stage's `outputs/` folder and described in that stage's README.
