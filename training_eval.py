"""Score a synthetic training-bot evaluation fixture."""
import json
import argparse
import math
from pathlib import Path

EXAMPLES = [
    {"id": "greeting", "expected": "hello", "actual": "Hello!"},
    {"id": "unknown", "expected": "I do not know", "actual": "I do not know."},
]


def normalize(text):
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Answers must be nonempty strings")
    normalized = text.strip().casefold().rstrip(".!?")
    if not normalized:
        raise ValueError("Answers must contain more than punctuation")
    return normalized


def score(examples):
    if not isinstance(examples, list) or not examples:
        raise ValueError("Expected a nonempty list of examples")
    rows = []
    seen = set()
    for example in examples:
        if not isinstance(example, dict) or set(example) != {"id", "expected", "actual"}:
            raise ValueError("Each example requires id, expected, and actual")
        identifier = example["id"]
        if not isinstance(identifier, str) or not identifier.strip() or identifier in seen:
            raise ValueError("Example IDs must be unique nonempty strings")
        seen.add(identifier)
        rows.append({"id": identifier,
                     "passed": normalize(example["expected"]) == normalize(example["actual"])})
    return {"examples": rows, "accuracy": sum(row["passed"] for row in rows) / len(rows)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, help="JSON evaluation array")
    parser.add_argument("--min-accuracy", type=float, default=1.0)
    args = parser.parse_args()
    if not math.isfinite(args.min_accuracy) or not 0 <= args.min_accuracy <= 1:
        parser.error("min-accuracy must be between 0 and 1")
    try:
        examples = json.loads(args.input.read_text(encoding="utf-8")) if args.input else EXAMPLES
        report = score(examples)
    except (ValueError, OSError, RecursionError) as exc:
        parser.exit(2, f"Invalid evaluation input: {exc}\n")
    print(json.dumps(report, indent=2))
    return 0 if report["accuracy"] >= args.min_accuracy else 1


if __name__ == "__main__":
    raise SystemExit(main())
