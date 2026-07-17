# Notebook quality guide

Use these checks when updating a lecture notebook or adding a new educational example.

## Before running

- Use a clean Python environment supported by the repository.
- Restart the kernel and run all cells from top to bottom.
- Fix random seeds where the library supports them.
- Keep datasets public, synthetic or properly attributed.

## Explanations

A useful notebook should explain:

1. the learning objective;
2. the dataset and feature meaning;
3. preprocessing choices;
4. the detector assumptions;
5. score direction and label convention;
6. threshold or contamination selection;
7. evaluation metrics;
8. observed failure cases;
9. the practical conclusion.

Avoid presenting one detector as universally best. Results depend on the anomaly definition, feature space, scaling, class balance and review cost.

## Code

- Keep cells focused and executable in sequence.
- Avoid hidden state from cells run out of order.
- Use clear variable names and brief comments for non-obvious steps.
- Separate data preparation, model fitting, scoring and evaluation.
- Do not suppress warnings without explaining why.
- Avoid absolute local file paths.

## Results

- Show more than accuracy for rare-event problems.
- Prefer precision, recall, F1, average precision and operational measures such as precision at k.
- Explain whether higher scores mean more or less anomalous.
- Report runtime when comparing computationally different methods.
- Discuss false positives and false negatives rather than showing only an aggregate score.

## Visuals

Every chart should have a descriptive title, labelled axes and a short interpretation. Use visualisations to support a conclusion, not only for decoration.

## Final review

Before committing a notebook:

- restart and run all cells;
- remove accidental debug output;
- confirm that links and paths work;
- check that no private data or credentials are present;
- record any important version-dependent behaviour;
- keep compatibility with the original Udemy lecture flow where relevant.

For a complete student project, also use the [project checklist](project-checklist.md).