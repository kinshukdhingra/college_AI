from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForTokenClassification, Trainer, TrainingArguments
import json

def load_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def tokenize_and_align_labels(examples, tokenizer):
    tokenized_inputs = tokenizer(examples['text'], truncation=True, padding=True, is_split_into_words=False)
    labels = []
    for i, text in enumerate(examples['text']):
        word_labels = [0] * len(text)
        for entity in examples["entities"][i]:
            start, end, label = entity["start"], entity["end"], entity["label"]
            word_labels[start:end] = [label] * (end - start)
        labels.append(word_labels)
    tokenized_inputs["labels"] = labels
    return tokenized_inputs

def fine_tune_ner():
    # Load data
    data = load_data("data/entities.json")
    tokenizer = AutoTokenizer.from_pretrained("dbmdz/bert-large-cased-finetuned-conll03-english")
    
    # Prepare dataset
    train_data = {"text": [item["text"] for item in data], "entities": [item["entities"] for item in data]}
    train_dataset = Dataset.from_dict(train_data)
    train_dataset = train_dataset.map(lambda examples: tokenize_and_align_labels(examples, tokenizer), batched=True)

    # Load pre-trained model
    model = AutoModelForTokenClassification.from_pretrained("dbmdz/bert-large-cased-finetuned-conll03-english", num_labels=3)
    
    # Training args
    training_args = TrainingArguments(
        output_dir="./models/fine_tuned_ner_model",
        num_train_epochs=3,
        per_device_train_batch_size=8,
        evaluation_strategy="epoch",
    )

    # Initialize Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
    )

    # Fine-tune
    trainer.train()

    # Save model
    model.save_pretrained("./models/fine_tuned_ner_model")
    tokenizer.save_pretrained("./models/fine_tuned_ner_model")
    print("Model fine-tuned and saved.")

if __name__ == "__main__":
    fine_tune_ner()
