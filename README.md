# SHIVA-LLM Objective 02

Reproducible simulation-based, one-step contextual-bandit policy optimization using HyperKT readiness predictions, with comparative evaluation, ablation studies, robustness analysis, and publication artifacts.

> **Scope statement.** All results in this repository are differences in a specified simulated utility. They do **not** establish causal instructional effects, long-term mastery gains, or sequential reinforcement-learning performance.

## Pipeline stages

| Stage | Description | Output archive | Status |
|---|---|---|---|
| 4A | Simulator construction | `objective02_stage4a_simulator.zip` | Complete |
| 4A-B | Robustness audit | `objective02_stage4ab_robustness_audit.zip` | Complete |
| 4A-C | Reward redesign | `objective02_stage4ac_reward_redesign.zip` | Complete |
| 4B | Policy optimization (depth-2 decision tree) | `objective02_stage4b_policy_optimization.zip` | Complete |
| 5 | Comparative evaluation | `objective02_stage5_comparative_evaluation.zip` | Complete |
| 6 | Ablation and statistical analysis | `objective02_stage6_ablation_analysis.zip` | Complete |
| 7 | Final reproducibility and publication package | `objective02_stage7_publication_package.zip` | Complete |

All notebooks run on Google Colab (Python 3, CPU runtime, 12–16 GB RAM recommended).

## Repository layout

```text
notebooks/   Colab notebooks, one folder per stage
src/         Reusable Python modules (if extracted from notebooks)
configs/     Experiment configuration files
results/     tables/ (CSV + LaTeX), figures/ (PNG + PDF), audits/
docs/        methodology, results summary, reproduction guide, limitations
manifests/   SHA-256 artifact manifests
```

## Headline result (held-out test, moderate assumed action effect)

32,522 interactions from 402 learners. See [docs/results_summary.md](docs/results_summary.md).

| Policy | Mean simulated reward |
|---|---|
| Learned decision tree | 0.583721 |
| Readiness rule | 0.579755 |
| Fixed hard | 0.558514 |
| Fixed medium | 0.520812 |
| Random | 0.507227 |
| Fixed easy | 0.444207 |

## Documentation

- [Methodology](docs/methodology.md)
- [Results summary](docs/results_summary.md)
- [Reproduction guide](docs/reproduction.md)
- [Limitations](docs/limitations.md)

## Related work

Part of a multi-objective research thesis. Objective 01 (HyperKT knowledge tracing) provides the readiness predictions used here.

## Citation

Citation details will be added once the Objective 02 manuscript is available.
