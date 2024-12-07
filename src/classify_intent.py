from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


class IntentClassifier:
    def __init__(self, model_name="distilbert-base-uncased",model_path=None):
        """
        Initialize the intent classifier with a pre-trained or fine-tuned model.
        -param model_name: Pre-trained transformer model name.
        -param model_path: Path to a fine-tuned model (if available).
        """
        if model_path:
            self.tokenizer = AutoTokenizer.from_pretrained(model_path)
            self.model = AutoModelForSequenceClassification.from_pretrained(model_path)
        else:
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForSequenceClassification.from_pretrained(model_name)

        #define intents
        self.intents = ["ask_vision", "greet", "ask_mission"]

    def predict_intent(self, user_input):
        """
        Predict the intent of a given user input.
        :param user_input: String containing the user's query.
        :return: Predicted intent as a string.
        """
        inputs = self.tokenizer(user_input, return_tensors="pt",truncation=True, padding=True)
        outputs = self.model(**inputs)
        logits = outputs.logits
        intent_idx = torch.argmax(logits, dim=1).item()
        return self.intents[intent_idx]
    
if __name__ == "__main__":
    classifier = IntentClassifier()

    # Test the classifier
    user_input = "whar are the business hours ?"
    predicted_intent = classifier.predict_intent(user_input)
    print(f"Predicted Intent: {predicted_intent}")