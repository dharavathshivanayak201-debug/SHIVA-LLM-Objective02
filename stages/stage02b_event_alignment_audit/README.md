# Stage 2B — Event alignment and split-reconciliation audit

**Notebook:** `SHIVA_LLM_Objective02_Stage2B_Event_Alignment_Audit_FIXED.ipynb` (final). The earlier version is kept in `superseded/`. · **Runtime:** Colab CPU · **Output archive:** `objective02_stage2b_audit.zip`

## Purpose
Checks whether the Stage 1 transitions and the Stage 2 HyperKT predictions can be joined safely. The notebook deliberately **refuses** to invent an alignment from user + skill + correctness matches.

## Findings (`outputs/stage2b_audit.json`)
| Check | Result |
|---|---|
| Stage 1 rows / learners | 342,643 / 4,097 |
| HyperKT rows / learners | 278,942 / 4,027 |
| Learners whose Stage 1 split ≠ HyperKT split | **1,694** |
| Event alignment verified | **false** (no authenticated crosswalk yet) |

`learner_split_crosswalk_counts.csv` cross-tabulates the two partitions. For example, 509 Stage 1 *test* learners are HyperKT *training* learners, so evaluating Stage 1 models on HyperKT data would leak.

## Decisions taken
1. The **HyperKT split is authoritative** for all later stages.
2. An event-level crosswalk `(split, window_index, position) → (user_id, order_id)` must be regenerated from the same sequence-construction run (Stage 2C).

## Outputs
`stage2b_audit.json`, `split_conflicts.csv` (per-learner conflicts), `learner_split_crosswalk_counts.csv`, `README.txt`.
