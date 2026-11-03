# Stage 2C — Authenticated event crosswalk

**Notebook:** `SHIVA_LLM_Objective02_Stage2C_Optimized.ipynb` (final, vectorised). The first version is in `superseded/`. · **Runtime:** Colab CPU, 8–12 GB RAM · **Output archive:** `objective02_stage2c_crosswalk.zip`

## Purpose
Recovers, for every HyperKT prediction, the original ASSISTments `user_id` and `order_id`. It does this by **re-running the Stage 1A/1B sequence construction** on the saved Parquet files and requiring an exact match with the saved NPZ sequences and the exported predictions.

## Inputs
`hyperkt_stage1.zip`, `hyperkt_stage2.zip`, `objective02_stage2_hyperkt_states.zip`.

## Verification result (`outputs/stage2c_audit.json`)
| Split | Events | Learners | Windows | Sequences match | Predictions aligned |
|---|---|---|---|---|---|
| Train | 222,562 | 3,222 | 3,706 | ✔ | ✔ |
| Validation | 23,858 | 403 | 445 | ✔ | ✔ |
| Test | 32,522 | 402 | 484 | ✔ | ✔ |

Status: **`event_alignment_verified`**. If any sequence had differed, the notebook would have stopped without producing a crosswalk.

## Output
`hyperkt_event_crosswalk.csv` (278,942 rows): `window_index, position, user_id, order_id, history_skill, history_correct, target_skill, target_correct, split, target_skill_pred, target_correct_pred, hyperkt_pred_correct`.

## Recorded limitations
No complete model-level temporal-leakage audit is claimed. Probabilities are not latent state vectors. Stage 1 Objective 02 splits remain incompatible.
