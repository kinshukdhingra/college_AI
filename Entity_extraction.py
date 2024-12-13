import spacy

# Load spaCy's English language model
nlp = spacy.load("models/fine_tuned_ner_model")

# Sample text
text = "I want to know about MBA or B.tech course at BABA FARID COLLEGE."

# Process the text
doc = nlp(text)

# Extract entities
for ent in doc.ents:
    print(f"Entity: {ent.text}, Label: {ent.label_}")
