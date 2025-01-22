import unittest
import sys
import os
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_path)

from src.Entity_extraction import entity_extraction  # Import your extraction function

class TestEntityExtractionBatch(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Define test cases for entity extraction."""
        cls.test_data = [
            {
                "text": "What are the admission requirements?",
                "expected_entities": [("admission requirements", "PROCESS")],
            },
            {
                "text": "What is the fee structure of B.Tech and M.Tech?",
                "expected_entities": [("fee structure", "PROCESS"),("B.Tech", "COURSE"), ("M.Tech", "COURSE")],
            },
            {
                "text": "Does the college have a library on campus?",
                "expected_entities": [("library", "CAMPUS_FACILITY")],
            },
            {
                "text": "Tell me something random without specific context.",
                "expected_entities": [],
            },
            {
                "text": "Who is the head of the Computer Science department?",
                "expected_entities": [
                    ("head", "FACULTY"),
                    ("Computer Science department", "DEPARTMENT"),
                ],
            },
        ]

    def test_entity_extraction(self):
        """Iterate over all test cases and validate results."""
        for case in self.test_data:
            with self.subTest(text=case["text"]):
                extracted_entities = entity_extraction(case["text"])
                self.assertEqual(
                    extracted_entities,
                    case["expected_entities"],
                    f"Failed for text: {case['text']}"
                )

if __name__ == "__main__":
    unittest.main()
