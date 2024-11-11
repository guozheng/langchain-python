from decouple import config
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

GOOGLE_GEMINI_KEY = config("GOOGLE_GEMINI_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_GEMINI_KEY)

st.title("Q & A With Gemini")

question = st.text_input("Your Question")

if st.button("Submit"):
    if question:
        response = llm.invoke(question)
        st.write(response.content)
    else:
        st.write("Please fill in all fields")
