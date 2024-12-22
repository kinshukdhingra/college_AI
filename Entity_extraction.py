import spacy

# Load spaCy's English language model
nlp = spacy.load("models/fine_tuned_ner_model")

# Sample text
text = "What is the fee structure?"

# Process the text
doc = nlp(text)

# Extract entities
for ent in doc.ents:
    print(f"Entity: {ent.text}, Label: {ent.label_}")
