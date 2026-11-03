# Results Summary

All numbers are read from the stage output files in this repository. The locked test split has 32,522 events from 402 learners. Rewards are **simulated utilities**.

## 1. Data and alignment
| Item | Value | Source |
|---|---|---|
| Raw / clean rows | 346,860 / 283,105 | Stage 1A `manifest.json` |
| HyperKT events (train / val / test) | 222,562 / 23,858 / 32,522 | Stage 2 audit |
| Events verified by crosswalk | 278,942 (100%) | Stage 2C audit |
| Matched to Stage 1 features | 275,272 | Stage 3 audit |
| Raw-adjacent transitions | 253,780 | Stage 3B audit |
| Learners with Stage 1 / HyperKT split conflict | 1,694 | Stage 2B audit |

## 2. Response model (Stage 4A)
| Split | Brier | Log loss | AUC |
|---|---|---|---|
| Train | 0.1755 | 0.5276 | 0.7711 |
| Validation | 0.1807 | 0.5398 | 0.7588 |
| Test | 0.1852 | 0.5509 | 0.7420 (95% CI 0.7237–0.7641) |

## 3. Policy comparison — moderate effect (Stage 4B / 5)
| Policy | Mean simulated reward | Regret |
|---|---|---|
| Learned (depth-2 tree) | 0.583721 | ≈ 0 |
| Readiness rule | 0.579755 | 0.003965 |
| Fixed hard | 0.558514 | 0.025207 |
| Fixed medium | 0.520812 | 0.062908 |
| Random | 0.507227 | 0.076494 |
| Fixed easy | 0.444207 | 0.139513 |

## 4. Paired learner-cluster bootstrap (500 reps, Stage 5)
| Scenario | Learned − readiness rule | Learned − best fixed | Learned − random |
|---|---|---|---|
| Zero | −0.0055 [−0.0063, −0.0047] | −0.0353 [−0.0385, −0.0324] | +0.0601 [+0.0536, +0.0669] |
| Small | −0.0015 [−0.0019, −0.0012] | −0.0128 [−0.0138, −0.0118] | +0.0671 [+0.0612, +0.0721] |
| Moderate | +0.0040 [+0.0035, +0.0044] | +0.0253 [+0.0227, +0.0280] | +0.0764 [+0.0723, +0.0804] |
| Large | +0.0084 [+0.0072, +0.0095] | +0.0450 [+0.0422, +0.0481] | +0.0793 [+0.0771, +0.0816] |

## 5. Reward-component ablation (moderate, Stage 6)
| Configuration | Learned − readiness rule [95% CI] | Learned − best fixed |
|---|---|---|
| Full reward | +0.003965 [0.003560, 0.004424] | +0.0252 |
| No correctness | +0.001820 [0.001644, 0.002009] | +0.0124 |
| No challenge | +0.017075 [0.015146, 0.019038] | −0.0187 |
| No suitability | −0.003666 [−0.004088, −0.003264] | −0.0049 |
| No cost | +0.003292 [0.002955, 0.003624] | +0.0186 |

## 6. Readiness-input perturbation (Stage 6)
| Perturbation | Actions changed | Mean reward |
|---|---|---|
| None | 0% | 0.5837 |
| Noise σ = 0.025 / 0.05 / 0.10 | 4.9% / 10.0% / 19.7% | 0.5831 / 0.5814 / 0.5740 |
| Bias +0.05 / −0.05 | 10.9% / 13.8% | 0.5819 / 0.5810 |
| Shuffle within learner | 42.7% | 0.5426 |

## 7. Calibration by readiness (test)
| Readiness | Events | Predicted | Observed |
|---|---|---|---|
| Low (< 0.4) | 4,665 | 23.67% | 28.64% |
| Medium (0.4–0.7) | 9,006 | 57.90% | 57.48% |
| High (≥ 0.7) | 18,851 | 81.48% | 79.91% |

## 8. Reproducibility
The frozen policy reproduces Stage 4B results in Stage 5, and Stage 5 results in Stages 6 and 7, with a maximum absolute difference of 5.55 × 10⁻¹⁷. The Stage 7 cross-stage integrity audit passed.

## Interpretation
- In the simulator, readiness-dependent difficulty selection beats every fixed action **only** when the assumed action effect is moderate or large.
- Its small edge over a hand-written readiness rule depends on the suitability term.
- The policy is sensitive to correctly ordered readiness input, which supports its dependence on HyperKT predictions. It does not show that HyperKT beats other knowledge-tracing models.
