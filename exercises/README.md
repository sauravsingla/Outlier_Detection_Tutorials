# Student Exercises

These exercises complement the Udemy lectures. Attempt each task before reading or adapting the reusable reference code.

## Exercise 1 — Understand the data

Choose one numerical dataset and answer:

1. What does one row represent?
2. Which observations can be extreme but valid?
3. Which values are impossible according to domain rules?
4. What is the cost of a false positive and a false negative?

## Exercise 2 — Univariate methods

For at least two numerical features:

- plot their distributions and box plots;
- detect outliers using IQR;
- detect outliers using a standard z-score;
- detect outliers using a robust z-score based on MAD;
- compare the observations identified by each method;
- explain the effect of skewness.

## Exercise 3 — Multivariate distance

Generate or select a two-dimensional dataset. Add points that are normal in each individual feature but unusual in combination. Compare:

- Euclidean distance;
- Mahalanobis distance;
- robust covariance.

Explain why univariate rules miss some multivariate anomalies.

## Exercise 4 — Neighbourhood methods

Compare KNN, DBSCAN and Local Outlier Factor on data containing:

- one dense cluster;
- one sparse cluster;
- isolated global anomalies;
- local anomalies close to the sparse cluster.

Explain which methods are sensitive to feature scaling and neighbourhood size.

## Exercise 5 — Isolation and boundary methods

Compare Isolation Forest and One-Class SVM. Report:

- preprocessing used;
- hyperparameters;
- anomaly-score direction;
- selected threshold;
- detected anomaly count;
- runtime;
- qualitative failure cases.

## Exercise 6 — High-dimensional methods

Add irrelevant features to a low-dimensional dataset and compare LOF, Isolation Forest and Feature Bagging. Explain how dimensionality affects distance concentration and local-density estimates.

## Exercise 7 — Autoencoder

Train an autoencoder primarily on normal observations. Plot reconstruction-error distributions for normal and anomalous validation observations. Select the threshold using validation data, not the final test set.

## Exercise 8 — Honest evaluation

For labelled anomalies, report:

- precision;
- recall;
- F1;
- average precision;
- ROC-AUC;
- precision at k;
- alert volume.

Explain why accuracy can be misleading.

## Capstone

Build an end-to-end anomaly-detection project on a public dataset. Include:

1. problem statement and operational objective;
2. data dictionary and licence/source;
3. exploratory analysis;
4. leakage-safe split;
5. statistical baseline;
6. at least two machine-learning detectors;
7. validation-based threshold policy;
8. evaluation and error analysis;
9. explanation of flagged records;
10. decision policy: retain, correct, cap, investigate or remove;
11. reproducible environment and instructions;
12. limitations, ethics and monitoring plan.

## Submission rubric

| Area | Weight |
|---|---:|
| Problem framing and domain reasoning | 15% |
| Reproducibility and code quality | 15% |
| Correct preprocessing and leakage prevention | 15% |
| Method comparison | 20% |
| Evaluation and thresholding | 20% |
| Interpretation and communication | 15% |