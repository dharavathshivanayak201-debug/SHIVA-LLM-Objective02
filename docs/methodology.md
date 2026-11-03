# Methodology

1. **Readiness input.** HyperKT predicted correctness for each learner interaction is used as a readiness signal.
2. **Simulator (Stage 4A–4A-C).** A one-step simulator assigns a simulated reward to each (context, action) pair, where actions are difficulty levels (easy, medium, hard). The reward combines correctness, challenge, suitability, and cost components. Assumed action effects are varied across zero, small, moderate, and large scenarios.
3. **Policy optimization (Stage 4B).** A depth-2 decision-tree policy is learned on training data and then frozen.
4. **Comparative evaluation (Stage 5).** The frozen policy is compared with a readiness rule, fixed-action, and random baselines on a held-out test partition. Uncertainty is estimated with 500 paired learner-cluster bootstrap resamples.
5. **Ablation and sensitivity (Stage 6).** Reward components are removed one at a time; readiness inputs are perturbed (noise, bias, within-learner shuffle); calibration is assessed by readiness group.
6. **Publication package (Stage 7).** Cross-stage reproducibility audit, publication tables and figures, and a SHA-256 manifest.

The test partition is never used to retrain or select the policy.
