# Complete Outlier Detection Algorithms A–Z: In Data Science

**Official student companion repository for the Udemy course created by Saurav Singla.**

This repository contains the Python code explained in the course **Complete Outlier Detection Algorithms A–Z: In Data Science**. The course introduces outlier, anomaly, novelty, and fraud detection from statistical foundations through machine learning and deep-learning methods.

> Course format: 3 sections · 18 lectures · approximately 1 hour 40 minutes · English

## Who this repository is for

- Udemy students following the original lectures
- Data scientists, data analysts, financial analysts, business analysts, software engineers, and technical managers
- Learners interested in anomaly detection, fraud detection, unusual patterns, and rare events
- Practitioners who want both classical explanations and modern reference implementations

## Course topics

The original course covers:

- Introduction, applications, causes, impact, and types of outliers
- Univariate, multivariate, and high-dimensional outlier detection
- Best practices and decisions around removing outliers
- Interquartile Range and standard-deviation methods
- KNN, DBSCAN, Local Outlier Factor, and clustering-based LOF
- Isolation Forest and Minimum Covariance Determinant
- One-Class SVM and Histogram-Based Outlier Detection
- Feature Bagging and Local Correlation Integral
- Angle-Based Outlier Detection
- Autoencoders for deep-learning-based anomaly detection

## Repository map

| Area | Purpose |
|---|---|
| `Tutorial_*.ipynb` | Original notebooks used with the Udemy lectures |
| `docs/course-syllabus.md` | Course-to-code learning map |
| `docs/course-roadmap.md` | Modern supplementary learning path |
| `src/outlier_detection/` | Reusable and tested reference implementation |
| `examples/` | Small end-to-end examples using open or synthetic data |
| `benchmarks/` | Reproducible detector comparisons |
| `tests/` | Automated tests for core utilities |

## How students should use the repository

1. Watch the relevant Udemy lecture.
2. Open the corresponding original `Tutorial_*.ipynb` notebook.
3. Run the notebook in Jupyter or Google Colab.
4. Change parameters and inspect how the detected outliers change.
5. Use the reusable package and benchmark material only after understanding the lecture implementation.

The original notebooks are preserved for continuity with the recorded course. New package code, tests, benchmarks, and production guidance are **supplementary material**, not replacements for the lectures.

## Quick start

```bash
git clone https://github.com/sauravsingla/Outlier_Detection_Tutorials.git
cd Outlier_Detection_Tutorials
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
python examples/quickstart.py
pytest
```

Students who only want to follow the original course notebooks can install the required packages directly in Jupyter or Colab and open the relevant tutorial.

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

Accuracy is usually misleading for rare anomalies. Prefer precision, recall, F1, average precision, ROC-AUC, precision at k, recall at k, and operational review volume. Fit preprocessing and thresholds only on training or validation data.

## Original course and modern extensions

The course was originally published in 2020. The repository now has two clearly separated tracks:

- **Original course track:** lecture-aligned notebooks and algorithms taught in the videos
- **Modern extension track:** reusable APIs, automated tests, reproducible benchmarks, threshold selection, monitoring, explainability, and production guidance

This separation ensures that existing students can still follow every lecture while external learners can use the repository as a current technical reference.

## Dataset note

The repository includes the Online Retail dataset archive used in the course material. Dataset files may have separate licenses or attribution requirements; verify source terms before redistributing them.

## Contributing

Bug fixes, clearer explanations, public datasets, benchmark results, and well-documented student exercises are welcome. See `CONTRIBUTING.md`.

## License

Code is released under the MIT License. Course videos and teaching content remain the intellectual property of their respective owner and platform.