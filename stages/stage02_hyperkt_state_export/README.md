# Stage 2 — Frozen HyperKT state export

**Notebook:** `SHIVA_LLM_Objective02_Stage2_HyperKT_State_Export.ipynb` · **Runtime:** Colab T4 GPU (CPU fallback) · **Output archive:** `objective02_stage2_hyperkt_states.zip`

## Purpose
Runs the **frozen** Objective 01 HyperKT model (gated variant, seed 42; no retraining) over every sequence and exports its **pre-response** probability that the learner answers the target skill correctly. This probability is the readiness signal used by the whole Objective 02 pipeline.

## Inputs (from the HyperKT Objective 01 repository)
1. Objective 01 Stage 2 ZIP (`train/val/test_sequences.npz`, `stage2_report.json`) — see Stage 1B.
2. Objective 01 Stage 3B ZIP with `hypergraph_repaired.npz`.
3. Objective 01 Stage 9E checkpoint ZIP with `HyperKT_gated_seed42/best.pt` (checkpoint SHA-256 `01d376c1…699bc5`).

Items 2 and 3 are Objective 01 artefacts and are not duplicated here.

## Method
- The Stage 9E architecture is re-declared verbatim and the checkpoint is loaded.
- Inputs: history skill, history correctness and target skill. **Target correctness is never an input.**
- Output: `hyperkt_pred_correct = sigmoid(logit)` per non-padded target.
- Split isolation is audited and a reproducibility manifest is written.

## Outputs
| File | Rows | Learners | Columns |
|---|---|---|---|
| `hyperkt_states_train.csv` | 222,562 | 3,222 | `split, window_index, position, user_id, target_skill, target_correct, hyperkt_pred_correct` |
| `hyperkt_states_val.csv` | 23,858 | 403 | same |
| `hyperkt_states_test.csv` | 32,522 | 402 | same |
| `stage2_export_audit.json` | — | — | model, checkpoint hash, event key, counts, cautions |

## Caveat
`(split, window_index, position)` are **window-local coordinates, not ASSISTments event IDs**. They cannot be joined to other tables until Stage 2C authenticates the mapping. The exported value is a one-dimensional probability, not the full latent knowledge state.
