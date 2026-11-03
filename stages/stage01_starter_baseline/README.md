# Stage 1 — Starter baseline (logged-action behaviour cloning)

**Notebook:** `SHIVA_LLM_Objective02_Colab_Stage1.ipynb` · **Runtime:** Colab, Python 3 (CPU is sufficient) · **Output archive:** `objective02_starter_results.zip`

## Purpose
First exploratory pass over the ASSISTments 2009 Skill Builder log. It builds an observational transition table and two diagnostic models so later stages have something concrete to audit. It is **not** a tutoring policy and makes no counterfactual claim.

## Inputs
- `data/skill_builder_data_corrected_collapsed.csv` (columns `user_id`, `problem_id`, `correct`, `order_id`; optional `skill_id`, `hint_count`).
- Optional HyperKT state CSV (`user_id`, `order_id`, `kt_probability`). When absent, the notebook falls back to a smoothed prior-accuracy proxy and prints a warning.

## Method
1. **Cleaning and ordering** — keep rows with valid `correct ∈ {0,1}` and numeric `order_id`; sort by learner and order.
2. **Learner-disjoint split** — 70 / 15 / 15 train/val/test by learner (seed 42).
3. **Causal state features** — `prior_attempts`, `prior_successes` and Laplace-smoothed `prior_accuracy = (successes+1)/(attempts+2)`; only past responses are used.
4. **Problem difficulty** — `1 − (correct+1)/(attempts+2)` per problem, estimated from **training rows only**.
5. **Action proxy** — the difficulty tercile (easy/medium/hard) of the **next observed problem**, shifted onto the current row as `logged_action`.
6. **Proxy reward** — `next_correct − 0.10 · |logged_action − 2·knowledge_state| / 2`.
7. **Behaviour cloning** — standardised multinomial logistic regression predicting `logged_action` from the state.
8. **Observational outcome model** — `HistGradientBoostingRegressor` for E[reward | state, action] (diagnostic only; confounded).

## Outputs (`outputs/objective02_artifacts/`)
| File | Description |
|---|---|
| `transitions.csv.gz` | Logged transitions: `user_id, order_id, split, knowledge_state, prior_accuracy, prior_attempts, logged_action, reward` (gzip-compressed) |
| `behavior_policy.joblib` | Behaviour-cloning logistic-regression pipeline |
| `observational_reward_model.joblib` | Gradient-boosted observational reward model |
| `README.txt` | Scope note written by the notebook |

## Why later stages replace it
Stage 2B showed that this 70/15/15 split is **incompatible** with the HyperKT 80/10/10 split (1,694 learners fall in different partitions), and Stage 3B showed the shifted difficulty bin is not an authenticated intervention. Stage 1 is retained for provenance; its split is discarded from Stage 3 onward.
