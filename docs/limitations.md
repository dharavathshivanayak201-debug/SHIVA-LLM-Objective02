# Limitations

1. **Simulated, one-step results.** Policy rewards are simulated contextual-bandit utilities, not observed learning outcomes. A depth-2 decision tree is not a sequential reinforcement-learning agent.
2. **Assumed action effects.** The easy / medium / hard effects, challenge credits, costs and reward weights are design assumptions; historical data do not identify them (Stage 3B).
3. **Conditional uncertainty.** Bootstrap intervals reflect learner sampling variability under the assumed simulator, not uncertainty about real instructional effects.
4. **Not universally robust.** The learned policy loses to the best fixed action under zero and small effects, and loses to the readiness rule when the suitability term is removed or challenge is weighted more heavily.
5. **Calibration gap.** The low-readiness group is under-predicted by about 5 percentage points (23.7% predicted vs 28.6% observed).
6. **Readiness input.** The policy uses the Stage 4A response-model probability, which is built on HyperKT. Perturbation results show dependence on that input, not superiority of HyperKT over other models.
7. **State representation.** HyperKT exports a one-dimensional correctness probability, not the full latent knowledge state.
8. **Transitions.** About 9% of exported next-event transitions are not adjacent in the raw log (253,780 of 278,942 are adjacent). The Stage 3 transitions are observed-event adjacency, not validated MDP dynamics.
9. **Post-hoc analyses.** Stage 5 and 6 robustness and ablation analyses use the test split for exploration only. They must not be used to revise the policy without a new hold-out.
10. **External artefacts.** The HyperKT checkpoint and hypergraph come from Objective 01 and are needed to regenerate Stage 2 from scratch.
