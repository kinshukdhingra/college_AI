# this code is to create Entity Training Data

# remove this file once the Training data is completed



text = "Do you offer a BTech program?"
entity = "BTech"
start = text.index(entity)
end = start + len(entity)
print(f"Entity: {entity}, Start: {start}, End: {end}")


import spacy
from spacy.training import offsets_to_biluo_tags

# Text and correct entity span
text = "Can I apply for a scholarship at BFCET?"
entities = [(33, 38, "COLLEGE")]  # Correct span

# Create a spaCy doc
nlp = spacy.blank("en")
doc = nlp.make_doc(text)

# Validate the alignment
print(offsets_to_biluo_tags(doc, entities))  # Should give correct BILUO tags
