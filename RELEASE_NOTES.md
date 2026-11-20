# Release candidate 0.1.0

This candidate provides a dependency-free response comparison API, JSON evaluation CLI, accuracy thresholds, package entrypoint, and Docker verification.

Run python -m unittest -v and python training_eval.py --input examples/evaluation.json --min-accuracy 0.5 before release. The eight synthetic comparisons produce accuracy 0.5. The paraphrase example deliberately shows the exact-comparison limitation. These examples cover selected failure modes and are not recorded model outputs.

The project uses the MIT License. A stable release is pending publication of a versioned artifact. Production evidence is pending execution in an identified target environment with representative model outputs.
