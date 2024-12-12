# Semantic Similarity For Intent Classification
# model = Fine Tuned Sentence-transformers

from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine

# load the Fine Tuned Model
# create a instance of model
model = SentenceTransformer("college_faq_model")

# Example FAQs or intents
# string representation of the Question
faqs = ["What is the admission process?", "What are the fees?", "Tell me about courses."]

# Encode FAQs
# turning the FAQs into vector ( or numerical form which is also know as embedings)
faq_embeddings = model.encode(faqs)

# Create a mapping of embeddings to FAQ labels
# creating a dictionary representation of the FAQs : Embedings
# zip() function combines the FAQs list and FAQ embeding list into pairs.
faq_to_embedding = {faq: embedding for faq, embedding in zip(faqs, faq_embeddings)}  # one line for loop

# Query from the user
# User's Question
query = "how can i apply?"


# Encode the query
# Converting the User Question into vector form (or Numerical form also known as embedings)
query_embedding = model.encode(query)

# intializing two variables to find the shortest distance
closest_faq = None
min_distance = float("inf")

# loops to find the Closest FAQs to the User Query
# comparing all the FAQs and user query Embedings
for faq, embedding in faq_to_embedding.items():
    distance = cosine(query_embedding, embedding)
    if distance < min_distance:
        min_distance = distance
        closest_faq = faq

# printing the closest FAQ
# output shortest distance FAQs
print(f"Closest FAQ: {closest_faq}")

# FAQs and intents are in dictionary form
# Each intent is connected to a query
faq_to_intent = {
    "What is the admission process?": "ADMISSION_QUERY",
    "What are the fees?": "FEE_QUERY",
    "Tell me about courses.": "COURSE_QUERY",
}

# Get the matched intent
matched_intent = faq_to_intent[closest_faq]
print(f"Matched Intent: {matched_intent}")

# ***********this is optional******************

# some pre-written response connected to the Intents
# when the intent is defined it chooses the relative response
intent_to_response = {
    "ADMISSION_QUERY": "The admission process involves filling out an online form.",
    "FEE_QUERY": "The fee structure depends on the course. Please specify the course.",
    "COURSE_QUERY": "We offer courses in Engineering, Science, and Arts."
}


response = intent_to_response[matched_intent]
print(f"Response: {response}")

# **************this is optional****************