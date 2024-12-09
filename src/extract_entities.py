from transformers import pipeline

class EntityExtractor:
    def __init__(self, model_name="dbmdz/bert-large-cased-finetuned-conll03-english"):
        """
        Initialize the entity extractor with a pre-trained model.
        :param model_name: Name of the pre-trained NER model.
        """
        self.ner_pipeline = pipeline("ner", model=model_name, aggregation_strategy="simple")

    def extract_entities(self, user_input):
        """
        Extract entities from the user input.
        :param user_input: String containing the user's query.
        :return: List of extracted entities with their labels.
        """
        results = self.ner_pipeline(user_input)
        entities = [{"entity": res["entity_group"], "text": res["word"], "score": res["score"]} for res in results]
        return entities


# Example usage
if __name__ == "__main__":
    extractor = EntityExtractor()

    # Test input
    user_input = "what is the vision of the BFCET?"
    extracted_entities = extractor.extract_entities(user_input)
    print("Extracted Entities:", extracted_entities)
