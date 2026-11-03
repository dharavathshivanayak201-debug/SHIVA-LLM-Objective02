# Stage 3B — Action semantics and temporal transition audit

**Notebook:** `SHIVA_LLM_Objective02_Stage3B_Action_Transition_Audit.ipynb` · **Runtime:** Colab CPU · **Inputs:** Stage 3 ZIP (+ raw CSV for adjacency checks) · **Output archive:** `objective02_stage3b_action_transition_audit.zip`

## Purpose
Decides whether the Stage 3 table can support offline reinforcement learning. It audits what the action means and whether transitions are truly adjacent in the raw log.

## Findings (`outputs/stage3b_audit.json`)
| Check | Result |
|---|---|
| HyperKT partitions disjoint | ✔ |
| Action provenance | Stage 1 next-event difficulty tercile, shifted to the current row |
| Action is an authenticated intervention | **✘** |
| Action aligned to the HyperKT target event | **✘ (not verified)** |
| Raw-log adjacency checked | ✔ — 253,780 of 278,942 exported transitions are truly adjacent |
| Offline RL policy evaluation ready | **✘** |

Action support is balanced (`action_counts.csv`). In the test split, for example, easy / medium / hard = 10,897 / 10,883 / 10,365.

## Consequence for the study design
Because historical actions are not real interventions, the project moved from offline RL to an **explicitly assumption-labelled one-step simulator** (Stage 4A). In that simulator, action effects are stated assumptions rather than estimates.

## Outputs
`stage3b_audit.json`, `action_counts.csv`, `split_transition_summary.csv` (events / learners / raw-adjacent per split), `event_transition_diagnostics.csv` (per-event gap and adjacency flags), `README.txt`.
