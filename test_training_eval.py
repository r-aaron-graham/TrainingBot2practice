import unittest
from training_eval import score, EXAMPLES


class EvaluationTests(unittest.TestCase):
    def test_fixture(self):
        self.assertEqual(score(EXAMPLES)["accuracy"], 1.0)

    def test_wrong_answer(self):
        self.assertEqual(score([{"id": "1", "expected": "hello", "actual": "goodbye"}])["accuracy"], 0.0)

    def test_invalid_input(self):
        for examples in ([], None, [{}], [{"id": "1", "expected": "", "actual": "text"}]):
            with self.subTest(examples=examples), self.assertRaises(ValueError):
                score(examples)

    def test_duplicate_ids(self):
        with self.assertRaises(ValueError):
            score([EXAMPLES[0], EXAMPLES[0]])


if __name__ == "__main__":
    unittest.main()
