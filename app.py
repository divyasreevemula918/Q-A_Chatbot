import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACKING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="Simple Q&A chatbot with ollama"
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant."),
        ("human", "{question}")
    ]
)
def generate_response(question,engine,temperature,max_tokens):
    llm=Ollama(model=engine)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer
    
st.title("Simple Q&A chatbot with ollama")
st.sidebar.title("Settings")
engine=st.sidebar.selectbox("select the model",["mistral"])
temperature=st.sidebar.slider("temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens=st.sidebar.slider("max tokens",min_value=50,max_value=300,value=150)
st.write("go ahead and ask a question about the world!")
user_input=st.text_input("you:")
if user_input:
    response=generate_response(user_input,engine,temperature,max_tokens)
    st.write(response)
else:
    st.write("please provide the user input")