import unittest

from Intent_classification import intent_prediction  # Replace with your actual function

class TestIntentClassification(unittest.TestCase):
    def setUp(self):
        """
        Set up test data for intent classification.
        """
        self.test_cases = [
            {"query": "What is the fee structure?", "expected_intent": "Fee Inquiry"},
            {"query": "Tell me about the college.", "expected_intent": "College Overview"},
            {"query": "How can I apply?", "expected_intent": "Admissions"},
            {"query": "Do you offer evening classes?", "expected_intent": "Courses Offered"},
            {"query": "What is the history of this institution?", "expected_intent": "College Overview"},
        ]

    def test_intent_classification(self):
        """
        Test the intent classification model.
        """
        for case in self.test_cases:
            with self.subTest(case=case):
                predicted_intent = intent_prediction(case["query"])
                self.assertEqual(predicted_intent, case["expected_intent"], 
                                 f"Query: {case['query']} - Expected: {case['expected_intent']}, Got: {predicted_intent}")

if __name__ == "__main__":
    unittest.main()
