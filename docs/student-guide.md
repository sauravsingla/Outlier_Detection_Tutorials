# Student Guide

This repository is the official coding companion for **Complete Outlier Detection Algorithms A–Z: In Data Science** by Saurav Singla.

## How to use the repository

1. Watch the related Udemy lecture.
2. Open the matching `Tutorial_*.ipynb` notebook.
3. Run the notebook from top to bottom before changing the code.
4. Recreate the important steps in a new notebook without copying.
5. Complete the practice questions in `exercises/README.md`.
6. Use the modern reference package only after understanding the lecture implementation.

## Recommended environments

### Google Colab

Upload a notebook to Colab and run the cells in order. Restart the runtime after installing or upgrading packages.

### Local Python

```bash
git clone https://github.com/sauravsingla/Outlier_Detection_Tutorials.git
cd Outlier_Detection_Tutorials
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -e ".[dev]"
jupyter lab
```

## Course-first learning path

### Stage 1 — Foundations

Understand the definition, applications, causes, impact and types of outliers. Distinguish genuine rare behaviour from data-quality problems.

### Stage 2 — Statistical detection

Study IQR, standard deviation and robust univariate analysis. Compare thresholds and inspect the effect of skewness.

### Stage 3 — Multivariate and local methods

Study KNN, DBSCAN, LOF, clustering-based methods, robust covariance and One-Class SVM. Scale features when distance or kernels are involved.

### Stage 4 — Isolation and ensemble methods

Study Isolation Forest, HBOS, Feature Bagging, ABOD and Local Correlation Integral. Compare global and local anomaly assumptions.

### Stage 5 — Deep learning

Study autoencoder reconstruction error and understand that a reconstruction score still requires a validation-based threshold.

### Stage 6 — Responsible decisions

Do not remove a record only because a model marks it as an outlier. Investigate whether it is an error, a legitimate extreme value, a rare class, fraud or a process change.

## Student completion checklist

- [ ] I can explain the difference between an outlier, anomaly, novelty and noise.
- [ ] I can apply IQR and standard-deviation rules.
- [ ] I can explain global versus local anomalies.
- [ ] I can compare KNN, DBSCAN and LOF.
- [ ] I can explain how Isolation Forest works.
- [ ] I can scale data correctly for One-Class SVM.
- [ ] I understand robust covariance and high-dimensional limitations.
- [ ] I can explain the role of contamination and thresholds.
- [ ] I can evaluate rare-event detection without relying on accuracy.
- [ ] I can justify whether an outlier should be retained, capped, corrected, investigated or removed.

## Asking for help

Before opening an issue, include:

- notebook name and cell number;
- Python version;
- package versions;
- complete error message;
- whether the issue occurs locally or in Colab;
- the smallest reproducible example.

Do not upload private, confidential or licensed datasets.