import streamlit as st
from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()

chat = ChatOpenAI(temperature=0.5,openai_api_key=os.getenv("OPENAI_API_KEY"),model='gpt-3.5-turbo')

st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey its Me YATO your Math Teacher, Let's Chat")
 
if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages']=[
        SystemMessage(content='I want you to act as a french math teacher. I will provide some mathematical equations or concepts, and it will be your job to explain them in easy-to-understand terms. This could include providing step-by-step instructions for solving a problem, demonstrating various techniques with visuals or suggesting online resources for further study. My first request is "I need help understanding how probability works."')
    ]

## Load OpenAI model and get respones
def get_chatmodel_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer = chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

input = st.text_input("Input: ",key="input")
response=get_chatmodel_response(input)

submit = st.button("Ask me Math question")

## Ask button is clicked
if submit:
    st.subheader("YATO :")
    st.write(response)