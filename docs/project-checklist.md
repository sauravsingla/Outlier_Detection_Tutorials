# Anomaly Detection Project Checklist

Use this checklist when completing a course exercise, adapting a notebook, or presenting an anomaly-detection project. It is designed to make the analysis reproducible and easier to review.

## 1. Problem definition

- [ ] State what an anomaly means in the problem domain.
- [ ] Explain whether the task is outlier detection, novelty detection, or supervised rare-event classification.
- [ ] Describe the practical cost of a false positive and a false negative.
- [ ] Identify who will review or act on an alert.

## 2. Data understanding

- [ ] Record the data source, collection period, unit of observation, and target population.
- [ ] Check missing values, duplicates, impossible values, and inconsistent units.
- [ ] Examine skew, heavy tails, seasonality, and subgroup differences.
- [ ] Confirm that no confidential, personal, or regulated data is committed to the repository.

## 3. Experimental design

- [ ] Separate training, validation, and test data before fitting preprocessing steps.
- [ ] Use a time-based split when future observations must not influence the past.
- [ ] Fix random seeds where the implementation supports them.
- [ ] Record Python and package versions.
- [ ] Establish a simple baseline before trying complex methods.

## 4. Preprocessing

- [ ] Explain how missing values are handled.
- [ ] Fit scaling, encoding, and feature selection only on training data.
- [ ] Justify any logarithmic or power transformation.
- [ ] Review whether distance-based methods are being distorted by feature scale.
- [ ] Keep an auditable mapping from transformed features to their original meaning.

## 5. Detector selection

- [ ] Match each selected detector to the structure of the data.
- [ ] Document the main assumptions and important hyperparameters.
- [ ] Compare at least two credible approaches when practical.
- [ ] Confirm whether larger or smaller scores represent more anomalous observations.
- [ ] Avoid treating a library default contamination value as a known anomaly rate.

## 6. Threshold selection

- [ ] Select the threshold using validation evidence, domain prevalence, or an alert-review budget.
- [ ] Report how results change under nearby threshold values.
- [ ] State the final expected alert volume.
- [ ] Keep score generation separate from the business decision threshold.

## 7. Evaluation

- [ ] Do not rely on accuracy when anomalies are rare.
- [ ] Report precision, recall, F1, and average precision where labels are available.
- [ ] Include precision at k when investigation capacity is limited.
- [ ] Measure runtime and memory when scalability matters.
- [ ] Inspect representative false positives and false negatives.
- [ ] Compare performance across meaningful subgroups when appropriate.

## 8. Interpretation

- [ ] Explain why selected observations received high anomaly scores.
- [ ] Distinguish data errors from valid but unusual observations.
- [ ] Avoid automatically deleting detected outliers.
- [ ] Document limitations and cases where the method is likely to fail.

## 9. Reproducibility

- [ ] Run the notebook from the first cell in a clean kernel.
- [ ] Remove hidden state and machine-specific file paths.
- [ ] Keep dependencies in `pyproject.toml` or an environment file.
- [ ] Save only outputs that help the learner understand the result.
- [ ] Verify that another person can follow the setup instructions.

## 10. Production considerations

- [ ] Define monitoring for data drift, score drift, and alert volume.
- [ ] Record retraining or recalibration triggers.
- [ ] Add human review for high-stakes decisions.
- [ ] Define fallback behaviour when data or model checks fail.
- [ ] Establish privacy, security, access-control, and incident-response requirements.

## Suggested project conclusion

A strong conclusion should answer four questions:

1. Which observations were flagged and how many?
2. Why was the selected detector and threshold appropriate?
3. What did the error analysis reveal?
4. What should a decision-maker do next?

Keep the conclusion understandable to a reader who has not seen the notebook code.