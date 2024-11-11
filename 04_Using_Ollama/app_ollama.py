from langchain_ollama.chat_models import ChatOllama

# llm = ChatOllama(model="gemma:2b")
llm = ChatOllama(model="llama3.2")

print("Q & A With Ollama")
print("=================")

question = "What's the currency of Thailand?"
print("Question: " + question)

response = llm.invoke(question)

print("Answer: " + response.content)
