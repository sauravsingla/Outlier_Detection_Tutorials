# Outlier Detection Tutorials

A practical, course-friendly reference for detecting anomalies in tabular data. The repository combines the original Udemy tutorial notebooks with reusable Python code, evaluation guidance, modern algorithms, and reproducible examples.

## What students learn

- How outliers differ from noise, novelty, fraud, rare events, and data errors
- Statistical methods: IQR, robust z-score, MAD, and Mahalanobis distance
- Classical machine learning: Isolation Forest, Local Outlier Factor, and One-Class SVM
- Modern approaches: Histogram-Based Outlier Score, autoencoders, and ensemble scoring
- How to choose contamination thresholds without leaking test labels
- How to evaluate highly imbalanced anomaly-detection systems
- How to explain, monitor, and deploy an outlier detector responsibly

## Repository map

| Area | Purpose |
|---|---|
| `Tutorial_*.ipynb` | Original Udemy lesson notebooks |
| `src/outlier_detection/` | Reusable, tested reference implementation |
| `examples/` | Small end-to-end examples that run without proprietary data |
| `benchmarks/` | Comparable experiments across detectors and datasets |
| `tests/` | Unit tests for core utilities |
| `docs/` | Course notes, method selection, and production guidance |

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

## Recommended learning path

1. Start with robust univariate statistics and visualization.
2. Learn multivariate distance-based detection.
3. Compare Isolation Forest, LOF, and One-Class SVM.
4. Use the benchmark to understand precision-recall trade-offs.
5. Study threshold selection, explainability, drift, and monitoring.
6. Apply the workflow to the Online Retail dataset or your own data.

## Method selection guide

| Situation | Good starting point | Important caution |
|---|---|---|
| One numeric feature | IQR or robust z-score | Skewed distributions may need transforms |
| Medium tabular dataset | Isolation Forest | Tune contamination on validation data |
| Local-density anomalies | LOF | Prediction mode differs from training mode |
| Clean reference data | One-Class SVM | Sensitive to scaling and hyperparameters |
| Large numeric dataset | HBOS | Assumes feature-wise independence |
| Complex nonlinear patterns | Autoencoder | Reconstruction error is not automatically calibrated |
| High-stakes use case | Ensemble plus human review | Track false positives and subgroup impact |

## Evaluation principles

Accuracy is usually misleading for rare anomalies. Prefer precision, recall, F1, average precision, ROC-AUC, precision at k, recall at k, and operational review volume. Fit preprocessing and thresholds only on training or validation data.

## Reproducibility

Examples use fixed random seeds and public or synthetic datasets. The original course notebooks are retained for continuity, while the package code provides cleaner APIs for external reuse.

## Course use

This repository supports the Udemy course material created by Saurav Singla. Students may use the code for learning and portfolio projects. Please cite the repository when adapting substantial parts for teaching or publication.

## Contributing

Bug fixes, additional public datasets, benchmark results, and well-explained tutorial notebooks are welcome. See `CONTRIBUTING.md`.

## License

Code is released under the MIT License. Dataset files may have their own licenses; verify the source terms before redistribution.
