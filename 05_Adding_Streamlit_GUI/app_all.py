from decouple import config
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
import concurrent.futures

OPENAI_KEY = config("OPENAI_KEY")
GOOGLE_GEMINI_KEY = config("GOOGLE_GEMINI_KEY")

llmOpenAI = ChatOpenAI(model="gpt-4o", api_key=OPENAI_KEY)
llmGemini = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_GEMINI_KEY)

st.title("Q & A With All LLMs")

question = st.text_input("Please Enter Your Question")

if st.button("Submit"):
    if question:
        # Create a ThreadPoolExecutor to run API calls in parallel
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Submit both API calls simultaneously
            future_openai = executor.submit(llmOpenAI.invoke, question)
            future_gemini = executor.submit(llmGemini.invoke, question)
            
            # Get results as they complete
            responseOpenAI = future_openai.result()
            responseGemini = future_gemini.result()
            
        # Display responses in separate rows
        st.markdown("**OpenAI Response**")
        st.text_area("", value=responseOpenAI.content, height=200, disabled=True)
        
        st.markdown("**Gemini Response**")
        st.text_area("", value=responseGemini.content, height=200, disabled=True)
    else:

        st.write("Please fill in all fields")
