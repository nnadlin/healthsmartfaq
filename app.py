import streamlit as st
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load Data & Embeddings
try:
    df = pd.read_csv("qa_dataset_with_embeddings.csv")
    question_embeddings = np.load("question_embeddings.npy") 
except FileNotFoundError:
    st.error("Data or embeddings file not found. Please upload them.")
    st.stop()

# Choose Embedding Model (Sentence Transformers is a good option)
model = SentenceTransformer('all-mpnet-base-v2')  # You can choose other models

# Streamlit Interface
st.title("PulseActive FAQ Chatbot")

user_question = st.text_input("Enter your question:")
search_button = st.button("Search")
clear_button = st.button("Clear")

if clear_button:
    user_question = ""
    st.experimental_rerun() # Clears the input field

if search_button and user_question:
    user_embedding = model.encode(user_question)
    similarities = cosine_similarity([user_embedding], question_embeddings)
    best_match_index = np.argmax(similarities)
    best_match_score = similarities[0][best_match_index]

    threshold = 0.6  # Experiment with this threshold value

    if best_match_score >= threshold:
        answer = df.iloc[best_match_index]['answer']  # Assuming your CSV has a 'answer' column
        st.write(f"**Answer:** {answer}")
        st.write(f"**Similarity Score:** {best_match_score:.2f}")

        # Optional: Add a helpfulness rating
        helpful = st.radio("Was this answer helpful?", ("Yes", "No"))
        if helpful == "Yes":
            st.write("Glad I could help!")  # Or store feedback
        elif helpful == "No":
            st.write("I'll try my best to improve. Please provide feedback if possible.") # Or store feedback

    else:
        st.write("I apologize, but I don't have information on that topic yet. Could you please ask other questions?")


# Optional: Display common FAQs (you'll need to define these)
st.subheader("Common FAQs")
# ... (Add code to display FAQs)

# Optional: Search bar to filter questions (more advanced)
# ... (Add code for question filtering)
