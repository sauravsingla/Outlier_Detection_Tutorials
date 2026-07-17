"""Small, dependable utilities used throughout the course examples."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

import numpy as np
from numpy.typing import ArrayLike, NDArray
from sklearn.base import clone
from sklearn.metrics import average_precision_score, precision_recall_fscore_support, roc_auc_score


class Detector(Protocol):
    """Protocol for scikit-learn style anomaly detectors."""

    def fit(self, x: ArrayLike, y: ArrayLike | None = None) -> object: ...


@dataclass(frozen=True)
class DetectionMetrics:
    precision: float
    recall: float
    f1: float
    average_precision: float
    roc_auc: float


def robust_zscore(values: ArrayLike, *, epsilon: float = 1e-12) -> NDArray[np.float64]:
    """Return median/MAD based z-scores.

    The factor 0.67448975 makes scores comparable with standard z-scores under
    an approximately normal distribution. Constant input returns zeros.
    """
    x = np.asarray(values, dtype=float)
    if x.ndim != 1:
        raise ValueError("robust_zscore expects a one-dimensional array")
    median = np.nanmedian(x)
    mad = np.nanmedian(np.abs(x - median))
    if not np.isfinite(mad) or mad <= epsilon:
        return np.zeros_like(x, dtype=float)
    return 0.67448975 * (x - median) / mad


def iqr_mask(values: ArrayLike, *, factor: float = 1.5) -> NDArray[np.bool_]:
    """Flag values outside Tukey's IQR fences."""
    if factor <= 0:
        raise ValueError("factor must be positive")
    x = np.asarray(values, dtype=float)
    if x.ndim != 1:
        raise ValueError("iqr_mask expects a one-dimensional array")
    q1, q3 = np.nanpercentile(x, [25, 75])
    spread = q3 - q1
    return (x < q1 - factor * spread) | (x > q3 + factor * spread)


def anomaly_scores(model: object, x: ArrayLike) -> NDArray[np.float64]:
    """Return scores where larger always means more anomalous."""
    if hasattr(model, "decision_function"):
        return -np.asarray(model.decision_function(x), dtype=float)
    if hasattr(model, "score_samples"):
        return -np.asarray(model.score_samples(x), dtype=float)
    raise TypeError("model must expose decision_function or score_samples")


def threshold_from_contamination(scores: ArrayLike, contamination: float) -> float:
    """Choose a score threshold using an expected anomaly fraction."""
    if not 0 < contamination < 0.5:
        raise ValueError("contamination must be between 0 and 0.5")
    values = np.asarray(scores, dtype=float)
    return float(np.quantile(values, 1.0 - contamination))


def fit_predict(
    estimator: Detector,
    x_train: ArrayLike,
    x_test: ArrayLike,
    *,
    contamination: float,
) -> tuple[object, NDArray[np.float64], NDArray[np.int64]]:
    """Fit a fresh estimator and produce calibrated binary predictions."""
    model = clone(estimator)
    model.fit(x_train)
    train_scores = anomaly_scores(model, x_train)
    threshold = threshold_from_contamination(train_scores, contamination)
    test_scores = anomaly_scores(model, x_test)
    predictions = (test_scores >= threshold).astype(np.int64)
    return model, test_scores, predictions


def evaluate(y_true: ArrayLike, scores: ArrayLike, predictions: ArrayLike) -> DetectionMetrics:
    """Evaluate anomaly scores and binary predictions.

    Labels use 1 for anomaly and 0 for normal observations.
    """
    y = np.asarray(y_true, dtype=int)
    score_values = np.asarray(scores, dtype=float)
    pred = np.asarray(predictions, dtype=int)
    precision, recall, f1, _ = precision_recall_fscore_support(
        y, pred, average="binary", zero_division=0
    )
    return DetectionMetrics(
        precision=float(precision),
        recall=float(recall),
        f1=float(f1),
        average_precision=float(average_precision_score(y, score_values)),
        roc_auc=float(roc_auc_score(y, score_values)),
    )
