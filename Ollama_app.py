import os
from dotenv import load_dotenv
load_dotenv() ## loading all the environment variable
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from langchain_ollama import ChatOllama

#langsmith tracking
os.environ["LANGSMITH_API_KEY"]=os.getenv("LANGSMITH_API_KEY")
os.environ["LANGSMITH_TRACING"]=os.getenv("LANGSMITH_TRACING")
os.environ["LANGSMITH_PROJECT"]=os.getenv("LANGSMITH_PROJECT")

prompt=ChatPromptTemplate.from_messages([
    ("system","You are helpful assistant. Please respond to the question asked."),
    ("user","Question:{question}")
])

def generate_response(question,engine,temperature):
    llm=ChatOllama(model=engine,temperature=temperature)
    output_parser=StrOutputParser()
    chain=prompt | llm | output_parser
    answer=chain.invoke({"question":question})
    return answer

engine=st.sidebar.selectbox("Select LLM Engine",["gemma:2b","llama3.1:8b"])
## Temprature adjustment - it means how creative the response should be
temperature=st.sidebar.slider("Temperature(creativity)",min_value=0.0,max_value=1.0,value=0.7)

st.write("Go ahead and ask your question!")
user_input=st.text_input("You: ")

if user_input:
    with st.spinner("Generating response..."):
        response=generate_response(user_input,engine,temperature)
        st.write(response)
else:
    st.write("Please enter a question to get started.")