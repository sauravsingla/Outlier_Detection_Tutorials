# Course Roadmap

## Module 1 — Foundations

Define outliers, anomalies, novelty, noise, rare classes, and data-quality errors. Discuss whether the objective is discovery, cleaning, fraud detection, monitoring, or scientific investigation.

## Module 2 — Exploratory detection

Use distributions, box plots, scatter plots, domain constraints, IQR fences, and robust z-scores. Never remove observations only because a chart looks unusual; first identify the data-generating reason.

## Module 3 — Multivariate statistical methods

Introduce covariance, Mahalanobis distance, robust covariance, dimensionality, and the limitations of Gaussian assumptions.

## Module 4 — Classical machine learning

Compare Isolation Forest, Local Outlier Factor, and One-Class SVM. Cover scaling, novelty mode, contamination, computational cost, and score direction.

## Module 5 — Modern methods

Introduce HBOS, Extended Isolation Forest, deep autoencoders, variational autoencoders, and representation-based detection. Explain when added complexity is justified and when it is not.

## Module 6 — Evaluation

Use labelled anomalies only for honest validation and testing. Focus on precision-recall curves, average precision, precision at k, recall at k, alert volume, investigation capacity, and cost-weighted metrics.

## Module 7 — Thresholding

Separate model scoring from operational decision thresholds. Compare quantile thresholds, validation-optimised thresholds, expected review capacity, and cost-based thresholds. Avoid selecting thresholds on the final test set.

## Module 8 — Explainability and investigation

Explain why an observation is unusual using feature deviations, local neighbours, reconstruction residuals, or post-hoc explanations. Preserve raw records and investigation context.

## Module 9 — Production design

Version preprocessing, model, threshold, and feature definitions together. Monitor score distributions, input drift, alert rates, delayed labels, false-positive burden, latency, and subgroup impact.

## Module 10 — Capstone

Build an end-to-end anomaly detector on a public dataset. Include a problem statement, leakage-safe split, baseline, modern comparator, threshold policy, evaluation report, error analysis, and deployment plan.

## Suggested capstone datasets

- UCI Online Retail for unusual customer or transaction behaviour
- Credit Card Fraud Detection for rare-event classification comparisons
- KDDCup99 or NSL-KDD for network intrusion exercises
- NAB time-series benchmark for streaming anomalies
- ODDS datasets for tabular anomaly benchmarks

Students should verify each dataset's license and usage terms before redistribution.
