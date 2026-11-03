# Results Summary

Values below are as reported from the verified stage outputs. The authoritative numbers are the CSV tables in `results/tables/` from the Stage 7 package.

## Bootstrap comparisons (moderate effect, 500 learner-cluster resamples)

| Comparison | Simulated advantage | 95% CI |
|---|---|---|
| Learned vs readiness rule | +0.003965 | [0.003547, 0.004403] (Stage 7) |
| Learned vs best fixed | +0.02527 | [0.02267, 0.02801] |
| Learned vs random | +0.07638 | [0.07226, 0.08037] |

The learned policy does **not** beat the best fixed action under zero and small assumed effects.

## Reward-component ablation (learned vs readiness rule, moderate effect)

| Configuration | Advantage | 95% CI |
|---|---|---|
| Full reward | +0.003965 | [0.003560, 0.004424] |
| Without correctness | +0.001820 | [0.001644, 0.002009] |
| Without challenge | +0.017075 | [0.015146, 0.019038] |
| Without suitability | −0.003666 | [−0.004088, −0.003264] |
| Without cost | +0.003292 | [0.002955, 0.003624] |

## Readiness-input robustness (% actions changed)

| Perturbation | Actions changed |
|---|---|
| Noise ±0.025 | 4.9% |
| Noise ±0.05 | 10.0% |
| Noise ±0.10 | 19.7% |
| Bias −0.05 | 13.8% |
| Bias +0.05 | 10.9% |
| Within-learner shuffle | 42.7% (mean reward 0.583721 → 0.542629) |

## Calibration by readiness group

| Readiness | Events | Predicted | Observed |
|---|---|---|---|
| Low | 4,665 | 23.67% | 28.64% |
| Medium | 9,006 | 57.90% | 57.48% |
| High | 18,851 | 81.48% | 79.91% |

## Reproducibility

The frozen policy reproduces Stage 4B/5 results in Stages 6 and 7 with a maximum numerical difference of 5.55 × 10⁻¹⁷.
