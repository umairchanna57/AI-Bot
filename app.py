
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv
from requests.exceptions import HTTPError
from langchain_huggingface import HuggingFaceEndpoint

repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
sec_key = "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"

# Set environment variable for Hugging Face token
import os
os.environ['umair'] = sec_key

llm = HuggingFaceEndpoint(repo_id=repo_id, max_length=128, temperature=0.7, api_key = sec_key)


prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title('My Bot')
input_text=st.text_input("Search the topic u want")

# openAI LLm 
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))