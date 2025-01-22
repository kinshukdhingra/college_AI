import unittest

import sys
sys.path.append(r"H:\AI_Assistant\college_AI")

from src.Intent_classification import intent_prediction  # import the intent classification function from src folder

class TestIntentClassification(unittest.TestCase):
    def setUp(self):
        """
        Set up test data for intent classification.
        """
        self.test_cases = [
            {"query": "How much does a program cost?", "expected_intent": "FEE_QUERY"},
            {"query": "Tell me about the college.", "expected_intent": "COLLEGE_OVERVIEW"},
            {"query": "What is the admission process?", "expected_intent": "ADMISSION_QUERY"},
            {"query": "what type of online programs or course are offered by the Baba Farid college?", "expected_intent": "ONLINE_LEARNING_AND_RESOURCES_QUERY"},
            {"query": "What is the history of this institution?", "expected_intent": "COLLEGE_OVERVIEW"},
        ]

    def test_intent_classification(self):
        """
        Test the intent classification model.
        """
        for case in self.test_cases:
            with self.subTest(case=case):
                predicted_intent = intent_prediction(case["query"])
                self.assertEqual(predicted_intent, case["expected_intent"],f"Query: {case['query']} - Expected: {case['expected_intent']}, Got: {predicted_intent}")

if __name__ == "__main__":
    unittest.main()
