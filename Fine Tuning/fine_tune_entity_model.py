import spacy
from spacy.training.example import Example
from spacy.util import minibatch
import sys
import os
# adding path to get access the folder files outside the current folder
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_path)

from training_data.entities_train_data import get_entities     # importing training data entities from training data

entites_data = get_entities()

# Step 1: Load the pre-trained model
nlp = spacy.load("en_core_web_md")

# Step 2: Get the NER pipeline component
ner = nlp.get_pipe("ner")

# Step 3: Add custom labels to the NER pipeline
custom_labels = ["INSTITUTE", "COURSE"]  # Add your custom labels here
for label in custom_labels:
    ner.add_label(label)

# Step 5: Disable other components during training
unaffected_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]

# Step 6: Train the model
with nlp.disable_pipes(*unaffected_pipes):  # Only train NER
    optimizer = nlp.resume_training()  # Resume training for pre-trained model
    for epoch in range(24):  # Number of training epochs
        losses = {}
        batches = minibatch(entites_data, size=2)
        for batch in batches:
            for text, annotations in batch:
                # Convert text and annotations into spaCy's Example format
                doc = nlp.make_doc(text)
                example = Example.from_dict(doc, annotations)
                # Update the model
                nlp.update([example], drop=0.3, losses=losses)
        print(f"Losses at epoch {epoch}: {losses}")

# Step 7: Save the fine-tuned model
nlp.to_disk("models/fine_tuned_ner_model")
print("Model fine-tuning complete!")
