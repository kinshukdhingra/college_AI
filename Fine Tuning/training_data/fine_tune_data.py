# training data for semantic Similarity to Fine Tune the Model.

from sentence_transformers import InputExample

# semantic Similarity examples to feed Model
train_examples = [
    # College Overview
    InputExample(texts=["What is the Vision of the College?", "Tell me about the College."], label=1.0),

    # Course Offered
    InputExample(texts=["What programs I can join after 12th?", "What courses are offered?"], label=1.0),

    # Admissions
    InputExample(texts=["How can I apply?", "What is the admission process?"], label=1.0),

    # Campus Facility
    InputExample(texts=["Does this college have library on campus?", "What are the facilities available here?"], label=1.0),

    # Faculty
    InputExample(texts=["Who is the principle of the colleg?", "Who is Head of Department Of SSD?"], label=1.0),
    # Departments
    InputExample(texts=["How many Departments do you have?", "Does this college have the Engineering Department?"], label=1.0),

    # Fees Structure
    InputExample(texts=["What is the fee Structure?", "How much does a program costs?"], label=1.0),

]