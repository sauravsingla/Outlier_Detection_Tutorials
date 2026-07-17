import numpy as np
import pytest
from sklearn.ensemble import IsolationForest

from outlier_detection import fit_predict, iqr_mask, robust_zscore, threshold_from_contamination


def test_robust_zscore_flags_extreme_value():
    scores = robust_zscore([10, 10, 11, 9, 10, 100])
    assert scores[-1] > 10


def test_robust_zscore_handles_constant_input():
    np.testing.assert_array_equal(robust_zscore([3, 3, 3]), np.zeros(3))


def test_iqr_mask_finds_obvious_outlier():
    mask = iqr_mask([1, 2, 2, 3, 100])
    assert mask.tolist() == [False, False, False, False, True]


def test_contamination_validation():
    with pytest.raises(ValueError):
        threshold_from_contamination([1, 2, 3], 0)


def test_fit_predict_returns_binary_labels():
    rng = np.random.default_rng(42)
    x_train = rng.normal(size=(100, 2))
    x_test = np.vstack([rng.normal(size=(20, 2)), [[10, 10]]])
    _, scores, predictions = fit_predict(
        IsolationForest(random_state=42),
        x_train,
        x_test,
        contamination=0.05,
    )
    assert scores.shape == (21,)
    assert set(predictions).issubset({0, 1})
    assert predictions[-1] == 1
