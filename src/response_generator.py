import sys
import os
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(src_path)

from src.Intent_classification import intent_prediction  # importing intent prediction from intent classification
from response_data.response import get_responses  # Import the get_response function from response_data

def generate_response(query):
    # Get intent from the classification model
    intent = intent_prediction(query)  # Assuming this function returns the intent
    response = get_responses(intent)  # Get response based on the intent
    return response

# creating the loops to create a conversation
while (user_query := input("You: ").lower()) not in ["quit", "back", "thats it", "bye"]:
    response = generate_response(user_query)
    print(response)
