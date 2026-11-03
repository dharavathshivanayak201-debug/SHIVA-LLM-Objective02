# Stage 3 — Multi-objective reward proxies and observed transitions

**Notebook:** `SHIVA_LLM_Objective02_Stage3_Reward_And_Transitions.ipynb` · **Runtime:** Colab CPU, 8–12 GB RAM · **Inputs:** Stage 2C crosswalk ZIP, Stage 1 starter ZIP · **Output archive:** `objective02_stage3_reward_dataset.zip`

## Purpose
Joins the authenticated HyperKT events to the Stage 1 features by exact `(user_id, order_id)`. It then defines transparent reward proxies and builds observed next-event transitions inside the HyperKT partitions.

## Join result (`outputs/stage3_audit.json`)
| Quantity | Value |
|---|---|
| Crosswalk events | 278,942 |
| Matched to Stage 1 rows | 275,272 |
| Unmatched (kept visible, no invented action) | 3,670 |
| Matched events whose old Stage 1 split conflicts | 111,284 |

Per split (`split_summary.csv`): train 222,562 events / 3,222 learners; validation 23,858 / 403; test 32,522 / 402.

## Reward proxies (weights 0.6 / 0.2 / 0.2)
- `r_performance` — observed correctness of the current target event.
- `r_efficiency_proxy` — `1 / (1 + prior_attempts)`: a history-only proxy, not real time or cost.
- `r_suitability_proxy` — `clip(1 − |p − 0.65| / 0.65, 0, 1)`, where `p` is the HyperKT prediction: an illustrative challenge-match proxy.

## Transitions
The state contains only the pre-response HyperKT estimate and prior-history features. `next_state` is the next **observed** event for the same learner in the same split. `observed_event_gap` records the gap in `order_id`, and `subset_terminal` marks the last exported event (not a true episode end).

## Outputs
| File | Description |
|---|---|
| `hyperkt_aligned_all_events.csv.gz` | All 278,942 aligned events with HyperKT prediction, Stage 1 features, reward components, next-state fields |
| `matched_action_diagnostics.csv.gz` | 275,272 events with a matched `logged_action` |
| `split_summary.csv` | Events, learners, matched actions and split conflicts per split |
| `stage3_audit.json` | Join statistics, reward definitions, readiness flags (`offline_policy_training_ready: false`) |

Both large CSVs are gzip-compressed. Read them directly with `pd.read_csv(path)`.
