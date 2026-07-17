# Troubleshooting

The original course notebooks were created in 2020. Package APIs, default parameters and notebook environments can change, so use this guide before changing the underlying lesson logic.

## Start with a clean environment

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

In Colab, restart the runtime after installing packages and then run all cells from the beginning.

## Common problems

### `ModuleNotFoundError`

Confirm that the virtual environment is active and install the project with `pip install -e ".[dev]"`. Avoid installing packages into a different Python interpreter.

### Dataset not found

Run notebooks from the repository root and use relative paths. Do not hard-code a personal desktop or Google Drive path. The included Online Retail archive remains course data; check its source terms before redistribution elsewhere.

### Deprecated NumPy or pandas code

Prefer current public APIs. Typical fixes include replacing removed NumPy aliases, avoiding chained assignment and using explicit column selection. Preserve the mathematical method demonstrated by the lecture.

### Different anomaly labels

Libraries do not use one universal convention. Scikit-learn estimators commonly return `-1` for outliers and `1` for inliers, while this repository's reusable evaluation utilities use `1` for anomaly and `0` for normal. Convert labels explicitly before evaluation.

### LOF cannot predict new data

`LocalOutlierFactor` behaves differently for training-set detection and novelty detection. Set `novelty=True` only when the fitted model must score unseen observations, and do not use novelty mode to predict the training set.

### One-Class SVM flags too many records

Scale features, review `nu` and `gamma`, remove impossible data errors first and validate the threshold on representative data.

### Autoencoder results change between runs

Set seeds where supported, document the hardware and software environment, and expect small numerical variation. Evaluate distributions and operational metrics rather than relying on one exact reconstruction value.

### Accuracy looks excellent but the detector is poor

An anomaly dataset can be more than 99% normal. Report precision, recall, F1, average precision, ROC-AUC, precision at k and alert volume.

## Reproducibility checklist

- [ ] Notebook runs from a fresh kernel.
- [ ] Data paths are relative.
- [ ] Random seeds are documented.
- [ ] Feature scaling is fitted only on training data.
- [ ] Threshold is selected without using final test labels.
- [ ] Anomaly-label convention is stated.
- [ ] Figures have titles and labelled axes.
- [ ] Conclusions explain limitations and false positives.

## Reporting a problem

Open a GitHub issue with the notebook, cell, environment, complete traceback and a minimal reproducible example. Remove all confidential data.