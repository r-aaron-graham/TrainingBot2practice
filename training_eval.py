"""Score a synthetic training-bot evaluation fixture."""
import json

EXAMPLES = [
    {"id": "greeting", "expected": "hello", "actual": "Hello!"},
    {"id": "unknown", "expected": "I do not know", "actual": "I do not know."},
]


def normalize(text):
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Answers must be nonempty strings")
    return text.strip().casefold().rstrip(".!?")


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


if __name__ == "__main__":
    print(json.dumps(score(EXAMPLES), indent=2))
