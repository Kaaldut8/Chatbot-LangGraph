import streamlit as st
from langgraph_backend import chatbot
from langchain.messages import HumanMessage

# st.session_state -> dict -> 
CONFIG = {"configurable": {"thread_id": "thread_1"}}

# loading the conversation history
if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

for message in st.session_state["message_history"]:
    with st.chat_message(message["role"]):
        st.text(message["content"])

#{'role': 'user', 'content': 'Hi'}
#{'role': 'assistant', 'content': 'Hello'}

user_input = st.chat_input("Type here")

if user_input:

    # first add the message to message_history
    st.session_state["message_history"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)

    response = chatbot.invoke({"messages": [HumanMessage(content=user_input)]}, config=CONFIG)

    ai_message = response["messages"][-1].content
    # first add the message to message_history
    st.session_state["message_history"].append({"role": "ai", "content": ai_message})
    with st.chat_message("ai"):
        st.text(ai_message)