from langchain_ollama.chat_models import ChatOllama
import streamlit as st

llm = ChatOllama(model="gemma:2b")

st.title("Q & A With Ollama")

question = st.text_input("Your Question")

if st.button("Submit"):
    if question:
        response = llm.invoke(question)
        st.write(response.content)
    else:
        st.write("Please fill in all fields")