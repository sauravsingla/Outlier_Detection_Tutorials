"""Compare common detectors on a reproducible synthetic dataset."""

from __future__ import annotations

from sklearn.datasets import make_blobs
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.neighbors import LocalOutlierFactor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import RobustScaler
from sklearn.svm import OneClassSVM

from outlier_detection import evaluate, fit_predict


def build_dataset():
    normal, _ = make_blobs(n_samples=1_000, centers=3, cluster_std=0.9, random_state=42)
    anomalies, _ = make_blobs(
        n_samples=50,
        centers=[(-8, 8), (8, -8)],
        cluster_std=1.4,
        random_state=7,
    )
    x = __import__("numpy").vstack([normal, anomalies])
    y = __import__("numpy").r_[__import__("numpy").zeros(len(normal)), __import__("numpy").ones(len(anomalies))]
    return train_test_split(x, y, test_size=0.35, stratify=y, random_state=42)


def main() -> None:
    x_train, x_test, _, y_test = build_dataset()
    detectors = {
        "isolation_forest": IsolationForest(n_estimators=300, random_state=42, n_jobs=-1),
        "local_outlier_factor": LocalOutlierFactor(n_neighbors=35, novelty=True),
        "one_class_svm": make_pipeline(RobustScaler(), OneClassSVM(gamma="scale", nu=0.05)),
    }

    print("model,precision,recall,f1,average_precision,roc_auc")
    for name, detector in detectors.items():
        _, scores, predictions = fit_predict(
            detector,
            x_train,
            x_test,
            contamination=0.05,
        )
        metrics = evaluate(y_test, scores, predictions)
        print(
            f"{name},{metrics.precision:.3f},{metrics.recall:.3f},"
            f"{metrics.f1:.3f},{metrics.average_precision:.3f},{metrics.roc_auc:.3f}"
        )


if __name__ == "__main__":
    main()
