from langchain_ollama import OllamaLLM ##imprort icin
from langchain_core.prompts import ChatPromptTemplate
model = OllamaLLM(model="gemma3") 
template = """Question : {question} 
Answer : Lets think step by step.""" 
prompt = ChatPromptTemplate.from_template(template) 

chain = prompt | model 

response = chain.invoke({"question": "Turkce bir fikra yaz"}) 

print(response) 

import streamlit as st 

st.title("Chatbot with Ollama") 

user_input = st.text_input("Type a question:") 

if user_input: 
    
    response = chain.invoke({"question": user_input})  
    
    st.write("Response:",  response)  
    




