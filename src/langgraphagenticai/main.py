import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI


def load_langgrah_agenticai_app():
    '''Initate the UI'''

    #LOAD UI
    ui =LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load nuser input from the UI")
        return
    
    user_message = st.chat_input("Enter your message: ")

    

