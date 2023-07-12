#integrate openai

import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_key

#streamlit
st.title("OpenAI Langchain Playground")
input_text=st.text_input("Search") 

#prompt template
first_input_prompt = PromptTemplate (
    input_variables=['firstvar'],
    template= "Tell me about celebrity {firstvar}"
)

#initialize
llm= OpenAI(temperature=0.8) #play w temperature
chain=LLMChain(llm=llm, prompt=first_input_prompt, verbose=True, output_key='person')

#prompt template
second_input_prompt = PromptTemplate (
    input_variables=['person'],
    template= "When was {person} born"
)

#initialize chain 2
chain2=LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key='dob')

parent_chain = SequentialChain(chains=[chain, chain2], input_variables=['firstvar'], output_variables=['person', 'dob'], verbose=True)


#to add memory, add another var


if input_text:
    st.write(parent_chain.run({'name': input_text}))
