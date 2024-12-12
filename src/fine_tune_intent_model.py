# Semantic Similarity For Intent Classification
# model = sentence-transformer


from sentence_transformers import SentenceTransformer, InputExample, losses
from torch.utils.data import DataLoader
from training_data.fine_tune_data import train_examples

# Load a pretrained model
model = SentenceTransformer('all-MiniLM-L6-v2')


'''
train_examples = [
    InputExample(texts=["How can I apply?", "What is the admission process?"], label=1.0),
    InputExample(texts=["What is the fee?", "Tell me about the admission process"], label=0.2),
]
'''
# Create a DataLoader
# select the batch 16-32 for laptops or small GPU to train the model
train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=16)

# Define the loss function
# it tells us how good or poorly the model is performing
# smaller the loss == better the accuracy of the college
train_loss = losses.CosineSimilarityLoss(model)

# Fine-tune the model
model.fit(train_objectives=[(train_dataloader, train_loss)], epochs=3, warmup_steps=100)

# Save the fine-tuned model
model.save("Fine_Tuned_Model")