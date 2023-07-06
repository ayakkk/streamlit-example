#integrate openai

import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_key

#streamlit
st.title("OpenAI Langchain Playground")
input_text=st.text_input("Search") 

#promp template
first_input_prompt = PromptTemplate (
    input_variables=['firstvar'],
    template= "Tell me about {firstvar}"
)

#initialize
llm= OpenAI(temperature=0.8) #play w temperature
chain=LLMChain(llm=llm, prompt=first_input_prompt, verbose=True)

if input_text:
    st.write(chain.run(input_text))