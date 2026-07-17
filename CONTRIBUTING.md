# Contributing

Thank you for helping improve this learning resource.

## Good contributions

- Correct a technical or statistical error
- Add a small, reproducible example using an openly available dataset
- Improve explanations for beginners without weakening technical accuracy
- Add a detector with a fair benchmark and documented limitations
- Improve tests, accessibility, or notebook reproducibility

## Development setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
ruff check src tests examples
pytest
python examples/quickstart.py
```

## Notebook standards

1. Explain the learning objective and dataset provenance.
2. Use fixed random seeds where appropriate.
3. Keep preprocessing leakage-safe.
4. Report more than accuracy for imbalanced data.
5. State the meaning and direction of anomaly scores.
6. Include limitations and likely failure modes.
7. Restart and run all cells before submission.
8. Do not commit secrets, credentials, or restricted datasets.

## Code standards

Keep functions focused, typed, and testable. Prefer scikit-learn-compatible interfaces. Add tests for new reusable utilities and avoid unnecessary dependencies.

## Commit style

Use small, descriptive commits such as `Explain LOF novelty mode`, `Add threshold calibration test`, or `Benchmark Isolation Forest on ODDS data`.
