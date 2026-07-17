"""Generate a small benchmark leaderboard on synthetic anomaly scenarios."""

from __future__ import annotations

import csv
from pathlib import Path

import numpy as np
from sklearn.datasets import make_blobs, make_moons
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.neighbors import LocalOutlierFactor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import RobustScaler
from sklearn.svm import OneClassSVM

from outlier_detection import evaluate, fit_predict


def datasets():
    rng = np.random.default_rng(42)

    normal, _ = make_blobs(n_samples=1_200, centers=4, cluster_std=0.8, random_state=42)
    outliers = rng.uniform(-10, 10, size=(60, 2))
    yield "clustered", np.vstack([normal, outliers]), np.r_[np.zeros(1_200), np.ones(60)]

    normal, _ = make_moons(n_samples=1_200, noise=0.08, random_state=42)
    outliers = rng.uniform([-1.5, -1.0], [2.5, 1.5], size=(60, 2))
    yield "nonlinear", np.vstack([normal, outliers]), np.r_[np.zeros(1_200), np.ones(60)]


def detectors():
    return {
        "Isolation Forest": IsolationForest(n_estimators=300, random_state=42, n_jobs=-1),
        "Local Outlier Factor": LocalOutlierFactor(n_neighbors=35, novelty=True),
        "One-Class SVM": make_pipeline(RobustScaler(), OneClassSVM(gamma="scale", nu=0.05)),
    }


def main() -> None:
    rows = []
    for dataset_name, x, y in datasets():
        x_train, x_test, _, y_test = train_test_split(
            x, y, test_size=0.35, stratify=y, random_state=42
        )
        for model_name, estimator in detectors().items():
            _, scores, predictions = fit_predict(
                estimator, x_train, x_test, contamination=float(y.mean())
            )
            result = evaluate(y_test, scores, predictions)
            rows.append(
                {
                    "dataset": dataset_name,
                    "model": model_name,
                    "precision": round(result.precision, 4),
                    "recall": round(result.recall, 4),
                    "f1": round(result.f1, 4),
                    "average_precision": round(result.average_precision, 4),
                    "roc_auc": round(result.roc_auc, 4),
                }
            )

    output = Path(__file__).with_name("leaderboard.csv")
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} benchmark rows to {output}")


if __name__ == "__main__":
    main()
