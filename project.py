import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchResults
from langchain.agents import initialize_agent,AgentType
from langchain.callbacks import StreamlitCallbackHandler

import os 
from dotenv import load_dotenv
load_dotenv()

#  Arxiv and Wiki tools
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, 
                                doc_content_chars_max=200)
arxiv = ArxivQueryRun(arxiv_wrapper = arxiv_wrapper)


wiki_wrapper = WikipediaAPIWrapper(top_k_results=1,
                                   doc_content_chars_max=200)
wiki = WikipediaQueryRun(wiki_wrapper = wiki_wrapper)


search = DuckDuckGoSearchResults(name="Search")


#streamlit title
st.title("Langchain - Search")

#Sidebar for Groq API Key
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")


# Initialize chat history if not present  
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "assistant", 
            "content": "Hi I am a chatbot who can search the web. How can I help you?"
        }

    ]

#display each message in chat bubble format
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"]) 


if prompt:=st.chat_input(placeholder="What is machine learning"):
    
    st.session_state.messages.append({
        "role":"user",
        "content":prompt
    })

    st.chat_message("user").write(prompt)  

    llm = ChatGroq(groq_api_key = api_key,
                   model_name = "Llama3-8b-8192",
                   streaming=True)





