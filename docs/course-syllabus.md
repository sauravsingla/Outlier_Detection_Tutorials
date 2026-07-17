# Original Udemy Course Syllabus

This document records the learning scope of **Complete Outlier Detection Algorithms A–Z: In Data Science**, created by Saurav Singla. It helps students connect the recorded lectures with the notebooks and supplementary repository material.

## Course overview

- 3 sections
- 18 lectures
- Approximately 1 hour 40 minutes
- Language: English
- Primary implementation language: Python

## Foundation lectures

1. Introduction to outliers
2. Applications of outlier detection
3. Causes and impact of outliers
4. Types of outliers
5. Methods for outlier detection
6. Outlier detection in univariate data
7. Outlier detection in multivariate data
8. Outlier detection in high-dimensional data
9. Outlier detection using deep learning
10. Best practices for outlier detection
11. How and when to remove outliers

## Algorithms taught

### Statistical methods

- Interquartile Range Method (IQR)
- Standard Deviation Method
- Minimum Covariance Determinant

### Neighbourhood and density methods

- K-Nearest Neighbours (KNN)
- DBSCAN
- Local Outlier Factor (LOF)
- Clustering-Based Local Outlier Factor
- Local Correlation Integral

### Isolation, boundary, and histogram methods

- Isolation Forest
- One-Class Support Vector Machine
- Histogram-Based Outlier Detection

### High-dimensional and ensemble methods

- Feature Bagging
- Angle-Based Outlier Detection

### Deep-learning method

- Autoencoders

## Suggested notebook workflow

The repository retains the original `Tutorial_*.ipynb` notebooks so that students can follow the recorded lessons without disruption. Before starting a notebook:

1. Read its title and first markdown cells to identify the associated method.
2. Run all cells once without modification.
3. Repeat the experiment with a different contamination level or threshold.
4. Explain each detected observation in plain language.
5. Compare the result with at least one alternative detector.

## Learning outcomes

By completing the course and notebooks, students should be able to:

- distinguish outliers from noise, novelty, fraud, and data-quality errors;
- select techniques for univariate, multivariate, and high-dimensional settings;
- implement common outlier-detection algorithms in Python;
- understand the strengths and limitations of statistical, machine-learning, and deep-learning approaches;
- decide whether an unusual observation should be investigated, transformed, capped, corrected, or removed;
- apply anomaly-detection methods to real-world analytical problems.

## Supplementary repository material

The package under `src/`, automated tests, benchmark scripts, and modern roadmap were added after the original recording. They are intended to reinforce the course with current engineering practices while preserving the original teaching sequence.