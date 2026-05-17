import streamlit as st
import requests


# Page title
st.title("🤖 RAG Customer Support Assistant")


# User input
query = st.text_input(
    "Ask your question"
)


# Button click
if st.button("Submit"):

    if query.strip():

        # Send request to FastAPI backend
        response = requests.post(
            "http://127.0.0.1:8000/chat",
            json={
                "query": query
            }
        )

        # Convert response JSON
        data = response.json()

        # Display answer
        st.subheader("AI Response")

        st.write(data["answer"])