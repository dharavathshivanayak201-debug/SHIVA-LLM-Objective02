# Methodology

Objective 02 asks whether HyperKT knowledge-tracing predictions can drive an adaptive choice of item difficulty. Real intervention logs do not exist in ASSISTments, so the study proceeds in two phases.

## Phase I — Data provenance and auditing (Stages 1–3B)
1. **Starter baseline (Stage 1).** Builds logged transitions from the raw log, using the next problem's difficulty tercile as an action proxy, and fits behaviour-cloning and observational reward models.
2. **HyperKT preprocessing (Stages 1A, 1B).** Reproduces the Objective 01 student-disjoint 80/10/10 split (seed 42), the training-only skill vocabulary, and 200-step target sequences.
3. **HyperKT state export (Stage 2).** Runs the frozen gated HyperKT checkpoint without retraining, giving one pre-response correctness probability per target event. Target correctness is never an input.
4. **Alignment audit (Stage 2B).** Shows that the Stage 1 and HyperKT partitions conflict for 1,694 learners and refuses heuristic joins. The HyperKT split becomes authoritative.
5. **Authenticated crosswalk (Stage 2C).** Replays the sequence construction and verifies all 278,942 predictions against original `(user_id, order_id)` events.
6. **Reward proxies and transitions (Stage 3).** Exact-key join with 275,272 matched events. Defines performance, efficiency and suitability proxies and builds observed next-event transitions.
7. **Action and transition audit (Stage 3B).** Finds that the logged action is not an authenticated intervention and is not aligned to the HyperKT target, so offline RL is **not** justified.

## Phase II — Assumption-labelled one-step contextual bandit (Stages 4A–7)
8. **Simulator (Stage 4A).** A logistic-regression response model on `hyperkt_pred_correct`, `prior_accuracy` and `prior_attempts` gives a calibrated `p_observed` (test AUC 0.742, Brier 0.185). Actions shift log-odds by +d / 0 / −d for easy / medium / hard.
9. **Robustness audit (Stage 4A-B).** Under the original reward, easy is optimal for 100% of contexts, so there is nothing to learn.
10. **Reward redesign (Stage 4A-C).** Uses the utility \(U_a = w_c q_a + w_m q_a c_a + w_s e^{-(q_a-\tau)^2/2h^2} - w_k k_a\). Four pre-declared designs were compared on validation, and the **balanced** design was selected (0.30 / 0.40 / 0.25 / 0.05, τ = 0.70, h = 0.20).
11. **Policy optimisation (Stage 4B).** Decision trees (depth 2–8) and logistic regression are trained to imitate the utility-maximising action under the moderate effect. Selection uses validation data only, and the **depth-2 tree** was frozen.
12. **Comparative evaluation (Stage 5).** The frozen policy is compared with readiness-rule, fixed and random baselines on the locked test split, using a 500-rep paired learner-cluster bootstrap, a 30-seed random baseline, reward-weight robustness and readiness strata.
13. **Ablations (Stage 6).** Leave-one-component-out reward ablations, readiness perturbations (noise, bias, within-learner shuffle) and readiness calibration. All are post-hoc and none changes the policy.
14. **Publication package (Stage 7).** Cross-stage integrity audit, 9 tables, 3 figures, a results draft and a SHA-256 manifest.

## Safeguards applied throughout
- Learner-disjoint partitions taken from HyperKT; Stage 1 partitions are discarded.
- Train-only fitting, validation-only selection and a single locked test evaluation.
- A zero-effect negative-control scenario in every comparison.
- Bootstrap resampling by learner, keeping repeated observations together.
- Every assumption (effects, credits, costs, weights) is recorded in JSON reports.
