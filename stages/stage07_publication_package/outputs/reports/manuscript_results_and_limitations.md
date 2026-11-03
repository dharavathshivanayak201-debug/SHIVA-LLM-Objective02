# Objective 02: Results and discussion (simulation-based)



## Study setting

The held-out test partition comprised 32,522 interactions from 402 learners. The frozen policy was a tree_depth_2 model, fitted on training contexts and selected using validation data. The environment was a one-step contextual bandit with assumed easy, medium, and hard action effects.



## Primary simulated comparison

Under the moderate assumed action effect, the learned policy achieved a mean simulated reward of 0.583721, versus 0.579755 for the readiness rule and 0.558514 for the best fixed action. The learned-minus-readiness difference was 0.003965; the learner-cluster bootstrap 95% interval was [0.003547, 0.004403]. The learned-minus-best-fixed difference was 0.025207, with bootstrap 95% interval [0.022672, 0.028005].



## Sensitivity

The learned-minus-best-fixed simulated reward differences across effect scenarios were: zero=-0.035293, small=-0.012779, moderate=+0.025207, large=+0.044907. The negative differences under weaker assumptions indicate that superiority is not robust across scenarios.



## Observational response calibration

The largest absolute readiness-group calibration gap was in the low group: predicted correctness 0.2367 versus observed 0.2864.



## Ablation interpretation

Reward-component ablations change the utility objective; they are preference-sensitivity tests rather than empirical component-effect identification. Readiness perturbations stress the single input to the frozen policy and do not constitute a comparison between alternative knowledge-tracing architectures.



## Limitations

The historical action labels were not authenticated instructional interventions. The simulator assumes action-dependent correctness, challenge credit, and effort cost, and does not identify causal effects or learner-state transitions. Bootstrap confidence intervals condition on those assumptions. The frozen model is a one-step contextual-bandit policy, not a validated sequential reinforcement-learning agent. No observed mastery improvement, long-term retention benefit, or real-world instructional effectiveness is established. Test-set robustness and ablation analyses are post-hoc and should not guide further model selection without a new holdout.



## Reproducibility

The maximum Stage 5-to-6 reward replication error was 5.551e-17. All input archive hashes and source-file provenance are recorded in the accompanying manifest.