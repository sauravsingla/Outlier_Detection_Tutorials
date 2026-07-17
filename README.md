<div align="center">

# Complete Outlier Detection Algorithms A–Z

### Official companion repository for the Udemy course by Saurav Singla

Practical anomaly-detection tutorials spanning statistical rules, classical machine learning, ensembles and deep learning.

[![CI](https://github.com/sauravsingla/Outlier_Detection_Tutorials/actions/workflows/ci.yml/badge.svg)](https://github.com/sauravsingla/Outlier_Detection_Tutorials/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)](pyproject.toml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange.svg)](https://jupyter.org/)
[![Code style: Ruff](https://img.shields.io/badge/code%20style-ruff-261230.svg)](https://docs.astral.sh/ruff/)

**3 sections · 18 lectures · approximately 1 hour 40 minutes · original course published in 2020**

[Start learning](#start-here) · [Explore algorithms](#algorithms-covered) · [Run the benchmark](#reproducible-benchmark) · [Practise](exercises/README.md) · [Get help](docs/troubleshooting.md)

</div>

---

## Why this repository exists

Outlier detection is not a single algorithm or a single threshold. The right approach depends on the data distribution, dimensionality, local structure, operational cost of false alarms and whether labelled anomalies are available.

This repository provides two complementary learning tracks:

1. **Original course track** — lecture-aligned notebooks that preserve continuity with the recorded Udemy course.
2. **Modern reference track** — reusable Python utilities, automated tests, exercises, benchmarks and current engineering guidance.

The goal is to help learners move from understanding an algorithm in a notebook to evaluating it responsibly and using it in a reproducible project.

## Start here

| Your goal | Begin with |
|---|---|
| Follow the Udemy course | Open the matching `Tutorial_*.ipynb` notebook and use the [course syllabus](docs/course-syllabus.md) |
| Learn the subject independently | Follow the [student guide](docs/student-guide.md) and [learning roadmap](docs/course-roadmap.md) |
| Try a working example quickly | Run [`examples/quickstart.py`](examples/quickstart.py) |
| Compare detectors | Run the [benchmark](#reproducible-benchmark) |
| Practise and build a portfolio project | Complete the [exercises and capstone](exercises/README.md), then use the [project checklist](docs/project-checklist.md) |
| Reuse the implementation | Explore [`src/outlier_detection/`](src/outlier_detection/) |
| Fix an environment or notebook error | Read the [troubleshooting guide](docs/troubleshooting.md) |

## What you will learn

By working through the course and repository, you will be able to:

- distinguish global, contextual and collective anomalies;
- identify the assumptions behind statistical, distance, density, isolation, kernel and reconstruction methods;
- implement univariate, multivariate and high-dimensional detection workflows;
- scale features and prepare data without leaking information;
- convert detector scores into documented operational decisions;
- evaluate rare-event models with suitable metrics rather than relying on accuracy;
- compare algorithms using reproducible experiments;
- explain why an observation was flagged and when it should **not** be removed;
- recognise common failure modes, including unstable thresholds and excessive false positives.

## Course coverage

The original course introduces:

- outlier definitions, applications, causes, impact and types;
- univariate, multivariate and high-dimensional detection;
- best practices and decisions around removing outliers;
- Interquartile Range and standard-deviation methods;
- K-Nearest Neighbours and DBSCAN;
- Local Outlier Factor and clustering-based local detection;
- Isolation Forest and Minimum Covariance Determinant;
- One-Class SVM and Histogram-Based Outlier Detection;
- Feature Bagging and Local Correlation Integral;
- Angle-Based Outlier Detection;
- autoencoders for nonlinear anomaly detection.

See [`docs/course-syllabus.md`](docs/course-syllabus.md) for the course-to-code map.

## Algorithms covered

| Family | Methods | Best suited to | Main caution |
|---|---|---|---|
| Statistical | IQR, standard deviation, robust z-score | One-dimensional numerical data | Distribution shape and skew matter |
| Distance based | KNN | Isolated points in scaled feature spaces | Cost grows with dataset size |
| Density based | LOF, DBSCAN, CBLOF | Local anomalies and cluster-shaped data | Neighbourhood parameters are sensitive |
| Covariance based | MCD / robust covariance | Approximately elliptical multivariate data | Assumptions weaken on complex distributions |
| Isolation based | Isolation Forest | General tabular data and large samples | Contamination and threshold still require validation |
| Kernel based | One-Class SVM | Novelty detection from clean reference data | Sensitive to scaling and hyperparameters |
| Histogram based | HBOS | Fast detection on numeric tabular data | Feature independence assumption can be restrictive |
| Ensemble based | Feature Bagging | High-dimensional data | Harder to interpret and tune |
| Angle based | ABOD | High-dimensional geometric anomalies | Exact variants can be computationally expensive |
| Deep learning | Autoencoder | Complex nonlinear patterns | Requires careful training and error calibration |

## Choosing a starting algorithm

```text
One numeric feature
└── IQR or robust z-score

Multivariate tabular data
├── General baseline ........ Isolation Forest
├── Local-density anomaly ... LOF
├── Cluster/noise structure . DBSCAN
└── Gaussian-like geometry .. Robust covariance / MCD

Clean examples of normal behaviour
└── One-Class SVM or autoencoder

High-dimensional data
└── Feature Bagging, ABOD variant or a validated ensemble
```

Treat this as a starting guide, not a universal ranking. Compare more than one credible baseline and validate the threshold against the real cost of investigation and missed anomalies.

## Repository structure

```text
Outlier_Detection_Tutorials/
├── Tutorial_*.ipynb          # Original Udemy lecture notebooks
├── src/outlier_detection/    # Reusable, tested Python implementation
├── examples/                 # Small end-to-end workflows
├── benchmarks/               # Reproducible detector comparison
├── exercises/                # Practice tasks and capstone project
├── tests/                    # Unit tests for reusable utilities
├── docs/
│   ├── course-syllabus.md     # Original course map
│   ├── student-guide.md       # Setup and study workflow
│   ├── course-roadmap.md      # Extended learning path
│   └── troubleshooting.md     # Common errors and fixes
├── pyproject.toml             # Package and development dependencies
└── .github/workflows/ci.yml   # Automated linting and tests
```

## Quick start

### Option 1: follow a notebook

Clone the repository, start Jupyter and open the notebook corresponding to the lecture:

```bash
git clone https://github.com/sauravsingla/Outlier_Detection_Tutorials.git
cd Outlier_Detection_Tutorials
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -e ".[dev]"
jupyter lab
```

Run notebook cells from the beginning in a clean kernel. Change one parameter at a time and record how the detected observations change.

### Option 2: run the reusable example

```bash
python examples/quickstart.py
```

The quickstart demonstrates a complete workflow using deterministic sample data and the reusable package API.

### Option 3: verify the project

```bash
ruff check src tests examples
pytest --cov=outlier_detection --cov-report=term-missing
```

The CI workflow runs on Python 3.10, 3.11 and 3.12.

## Reproducible benchmark

Use the benchmark to compare detectors under the same dataset split, scaling and evaluation policy:

```bash
python benchmarks/benchmark.py
```

A useful benchmark should report more than one metric:

| Metric | Why it matters |
|---|---|
| Precision | How many reviewed alerts are genuine anomalies |
| Recall | How many known anomalies are detected |
| F1 | Balance between precision and recall |
| Average precision / PR-AUC | Ranking quality for rare positive events |
| ROC-AUC | Broad ranking measure; interpret carefully with severe imbalance |
| Precision at k | Quality within a fixed investigation budget |
| Runtime | Operational feasibility and scalability |

Do not copy benchmark numbers across datasets as if they were universal. Performance depends on the anomaly definition, preprocessing, class balance, score orientation and threshold policy.

## A responsible anomaly-detection workflow

1. Define what an anomaly means in the domain.
2. Separate training, validation and test data before fitting preprocessing.
3. Establish a simple baseline.
4. Train multiple credible detectors where appropriate.
5. Confirm whether a higher or lower score means “more anomalous”.
6. Select thresholds using validation evidence or an operational review budget.
7. Evaluate ranking quality, classification quality and alert volume.
8. Review false positives and false negatives with domain experts.
9. Monitor score distribution, data drift and alert rates after deployment.
10. Record assumptions, limitations and retraining triggers.

## Should an outlier be removed?

**Not automatically.** A flagged observation may be:

- a data-entry or measurement error to correct;
- a duplicate or impossible record to remove;
- a valid extreme value to retain;
- a fraud, safety or security event to investigate;
- a rare class requiring a different model;
- evidence of process, sensor or population drift.

Removal must be justified by domain knowledge and documented. Blindly deleting unusual values can erase the exact behaviour the analysis is meant to discover.

## Real-world applications

The same principles apply across many domains:

- financial fraud and anti-money-laundering investigation;
- payment and retail transaction monitoring;
- network intrusion and account-takeover detection;
- manufacturing defects and predictive maintenance;
- IoT and sensor-health monitoring;
- insurance claim review;
- healthcare quality and diagnostic-support analysis;
- data-quality validation and pipeline monitoring.

High-stakes use cases require human review, subgroup analysis, privacy safeguards and explicit escalation policies.

## Student practice

The [`exercises`](exercises/README.md) progress from basic statistical detection to multivariate modelling and a complete capstone. Use the [`project checklist`](docs/project-checklist.md) to review the final work before sharing it. For every exercise, learners should document:

- the business or analytical objective;
- preprocessing choices;
- detector assumptions;
- score and label conventions;
- threshold-selection method;
- suitable evaluation metrics;
- observed failure cases;
- a concise conclusion understandable to a non-specialist.

## Common questions

<details>
<summary><strong>Which notebook should I open first?</strong></summary>

Use the lecture mapping in [`docs/course-syllabus.md`](docs/course-syllabus.md). Learners studying independently should begin with the fundamentals in the student guide.
</details>

<details>
<summary><strong>Why do my results differ from the lecture?</strong></summary>

Differences can come from package versions, random initialisation, changed defaults, row ordering or floating-point behaviour. Fix random seeds where supported and compare the overall pattern rather than expecting every number to match exactly.
</details>

<details>
<summary><strong>How should I choose contamination?</strong></summary>

Do not choose it only because a library requires a value. Use labelled validation data, known operational prevalence, an investigation budget or sensitivity analysis. Document the assumption.
</details>

<details>
<summary><strong>Why is accuracy usually a poor metric?</strong></summary>

When anomalies are rare, a model can achieve very high accuracy by predicting every observation as normal. Precision, recall, average precision and top-k measures are generally more informative.
</details>

<details>
<summary><strong>Can I use these examples directly in production?</strong></summary>

Use them as educational and reference implementations. Production systems additionally need validated data contracts, monitoring, security controls, model governance, performance testing and an incident-response process.
</details>

## Data and reproducibility

The repository includes the Online Retail archive used in the original course material. Dataset files may have licences and attribution requirements separate from the source code. Verify the source terms before redistribution or commercial use.

Never commit private, confidential or regulated data. Use public or synthetic data when contributing examples.

## Contributing

Contributions are welcome when they improve correctness, clarity or reproducibility. Good contributions include:

- bug fixes with a regression test;
- clearer notebook explanations;
- properly attributed public datasets;
- reproducible benchmark additions;
- well-scoped exercises and solution notes;
- documentation for assumptions and limitations.

Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a pull request. When reporting a notebook problem, include the notebook name, cell number, Python version, package versions and complete traceback.

## Citation

To cite this repository in teaching material or technical work:

```bibtex
@software{singla_outlier_detection_tutorials,
  author  = {Saurav Singla},
  title   = {Complete Outlier Detection Algorithms A-Z: In Data Science},
  url     = {https://github.com/sauravsingla/Outlier_Detection_Tutorials},
  note    = {Udemy course companion repository}
}
```

## Acknowledgements

This educational project builds on the broader Python data-science ecosystem, including Jupyter, NumPy, pandas, scikit-learn and research contributions from the anomaly-detection community. Algorithm names and implementations remain attributable to their original authors and maintainers.

## License

Repository source code is released under the [MIT License](LICENSE). Course videos, narration, slides and other teaching content remain the intellectual property of their respective owner and platform.

---

<div align="center">

**Learn the assumptions. Run the experiment. Inspect the mistakes. Document the decision.**

</div>