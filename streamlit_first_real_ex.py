import streamlit as st
import os

#F8F4F9

#from langchain.llms import OpenAI
#from langchain import PromptTemplate
#from langchain.chains import LLMChain  

##from langchain.chains import SequentialChain

st.title("translator")

selected_language = st.radio(
    "Pick a language to translate into",
    ('English', 'French', 'Mandarin')
)
    
input_text=st.text_input(":fried_egg:") 




####### set up  

# os.environ["OPENAI_API_KEY"] = ''

# template = '''Translate '{sentence}' into {target_language} '''

# language_prompt = PromptTemplate(
#    input_variables=["sentence", 'target_language'],
#    template=template
# )


#language_prompt.format(sentence="this is a test", target_language='japanese')
#language_prompt.format(sentence="this is a test", target_language=selected_language)

######chain 
# llm = OpenAI(temperature=0.7)
# chain2 = LLMChain(llm=llm, prompt=language_prompt)
# #if more than 1 parameter, need to use keys
# chain2({'sentence': "Hello", 'target_language':'Japanese'})


#verified until openAI
#further implementation idea: allow multiple languages selection
