# Complete Outlier Detection Algorithms A–Z: In Data Science

**Official student companion repository for the Udemy course created by Saurav Singla.**

This repository contains the Python code explained in the course **Complete Outlier Detection Algorithms A–Z: In Data Science**. It combines the original lecture notebooks with student exercises, reproducible examples, tested utilities and modern professional guidance.

> Course format: 3 sections · 18 lectures · approximately 1 hour 40 minutes · English · free enrolment shown on the course page

## Start here

| I am... | Recommended starting point |
|---|---|
| Following the Udemy videos | Open the matching `Tutorial_*.ipynb` notebook |
| New to Python or notebooks | Read [`docs/student-guide.md`](docs/student-guide.md) |
| Looking for the original syllabus | Read [`docs/course-syllabus.md`](docs/course-syllabus.md) |
| Ready to practise | Complete [`exercises/README.md`](exercises/README.md) |
| Facing an error | Use [`docs/troubleshooting.md`](docs/troubleshooting.md) |
| Building a professional project | Run `examples/quickstart.py` and the benchmark |

## Who this repository is for

- Udemy students following the original lectures
- Data scientists, data analysts, financial analysts and business analysts
- Software engineers and technical managers working with unusual behaviour
- Learners interested in anomaly detection, fraud detection and rare events
- Practitioners who want both classical explanations and modern implementations

## Course topics

The original course covers:

- Introduction, applications, causes, impact and types of outliers
- Univariate, multivariate and high-dimensional outlier detection
- Best practices and decisions around removing outliers
- Interquartile Range and standard-deviation methods
- KNN, DBSCAN, Local Outlier Factor and clustering-based LOF
- Isolation Forest and Minimum Covariance Determinant
- One-Class SVM and Histogram-Based Outlier Detection
- Feature Bagging and Local Correlation Integral
- Angle-Based Outlier Detection
- Autoencoders for deep-learning-based anomaly detection

## Repository map

| Area | Purpose |
|---|---|
| `Tutorial_*.ipynb` | Original notebooks used with the Udemy lectures |
| `docs/course-syllabus.md` | Original course-to-code learning map |
| `docs/student-guide.md` | Setup, workflow and completion checklist |
| `docs/troubleshooting.md` | Solutions for common notebook and package issues |
| `docs/course-roadmap.md` | Modern supplementary learning path |
| `exercises/` | Progressive practice tasks and capstone rubric |
| `src/outlier_detection/` | Reusable and tested reference implementation |
| `examples/` | Small end-to-end examples using open or synthetic data |
| `benchmarks/` | Reproducible detector comparisons |
| `tests/` | Automated tests for core utilities |

## How students should use the repository

1. Watch the relevant Udemy lecture.
2. Open the corresponding original `Tutorial_*.ipynb` notebook.
3. Run it from a clean Jupyter or Google Colab session.
4. Change one parameter at a time and explain the result.
5. Recreate the important steps without copying.
6. Complete the related student exercise.
7. Use the reusable package and benchmark after understanding the lecture implementation.

The original notebooks are preserved for continuity with the recorded course. New package code, tests, benchmarks and production guidance are **supplementary material**, not replacements for the lectures.

## Quick start

```bash
git clone https://github.com/sauravsingla/Outlier_Detection_Tutorials.git
cd Outlier_Detection_Tutorials
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -e ".[dev]"
python examples/quickstart.py
pytest
```

Students who only want to follow the original notebooks can upload the relevant notebook to Colab. Restart the runtime after installing packages and run all cells from the beginning.

## Algorithm selection guide

| Situation | Good starting point | Important caution |
|---|---|---|
| One numeric feature | IQR or robust z-score | Skewed distributions may require transformation |
| Multivariate Gaussian-like data | Robust covariance / MCD | Sensitive to distributional assumptions |
| Local-density anomalies | LOF or KNN | Scaling and neighbourhood size matter |
| Cluster-shaped data | DBSCAN | Parameter selection strongly affects noise labels |
| General tabular anomaly detection | Isolation Forest | Validate contamination and threshold choices |
| Clean reference data | One-Class SVM | Sensitive to scaling and hyperparameters |
| Large numeric datasets | HBOS | Assumes limited feature dependence |
| High-dimensional sparse anomalies | Feature Bagging or ABOD variants | Computational cost can be high |
| Complex nonlinear patterns | Autoencoder | Reconstruction error requires careful calibration |
| High-stakes detection | Ensemble plus human review | Monitor false positives and subgroup impact |

## Evaluation principles

Accuracy is usually misleading for rare anomalies. Prefer precision, recall, F1, average precision, ROC-AUC, precision at k, recall at k and operational review volume. Fit preprocessing and thresholds only on training or validation data.

A model score and an operational decision are not the same thing. Document the score direction, label convention, contamination assumption and threshold policy.

## Should an outlier be removed?

Not automatically. A flagged observation can be:

- a data-entry or measurement error to correct;
- a duplicate or impossible record to remove;
- a valid extreme value to retain;
- a fraud or security event to investigate;
- a rare class that needs a different model;
- evidence of process or population drift.

Every removal decision should have a documented domain reason.

## Original course and modern extensions

The course was originally published in 2020. The repository has two clearly separated tracks:

- **Original course track:** lecture-aligned notebooks and algorithms taught in the videos
- **Modern extension track:** reusable APIs, automated tests, reproducible benchmarks, threshold selection, monitoring, explainability and production guidance

This separation ensures that existing students can follow every lecture while external learners can use the repository as a current technical reference.

## Quality standard

A course contribution is considered complete only when it:

- runs from a clean environment;
- uses public, synthetic or properly attributed data;
- explains the objective and method assumptions;
- avoids preprocessing and threshold leakage;
- states the anomaly-label convention;
- includes interpretable figures and conclusions;
- reports suitable rare-event metrics;
- documents limitations and responsible use;
- includes a test or reproducible execution path where practical.

## Dataset note

The repository includes the Online Retail dataset archive used in the course material. Dataset files may have separate licences or attribution requirements; verify source terms before redistributing them.

## Contributing

Bug fixes, clearer explanations, public datasets, benchmark results and well-documented student exercises are welcome. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

When reporting a notebook problem, include the notebook name, cell number, Python version, package versions and complete traceback. Do not upload confidential data.

## License

Code is released under the MIT License. Course videos and teaching content remain the intellectual property of their respective owner and platform.