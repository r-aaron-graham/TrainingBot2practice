# Training Bot Evaluation Practice

A local example for scoring expected and actual chatbot responses. This repository began empty. The example uses two synthetic responses to demonstrate a repeatable evaluation workflow.

## Run

Python 3.12 and the standard library are sufficient.

```sh
python training_eval.py
python -m unittest -v
```

The bundled fixture returns two passing examples and accuracy 1.0. This measures agreement on the supplied synthetic responses. It does not measure a trained model's accuracy.

## Evaluation contract

Call score(examples) with a nonempty list of records containing exactly id, expected, and actual. IDs must be unique nonempty strings. Answers must be nonempty strings. Comparison ignores case, surrounding whitespace, and trailing periods, exclamation marks, and question marks. Other wording changes fail comparison.

Use separately labeled, representative evaluation data before drawing conclusions about a deployed bot. Model training, provider integration, semantic scoring, and production deployment remain extension points.

## File evaluation and deployment

Run `python training_eval.py --input examples.json --min-accuracy 0.9`. Exit codes are 0 when the threshold is met, 1 when accuracy is below the threshold, and 2 for invalid input. Punctuation-only answers are rejected. Install with `python -m pip install .` and use `training-eval`.

The deployment workflow verifies the installed command outside the checkout, scans application code with Bandit, and runs the tests and fixture in a network-isolated container. Build locally with `docker build -t training-eval .`. See SECURITY.md for reporting and data-handling scope.

## License

Licensed under the MIT License. See LICENSE for the full terms.
