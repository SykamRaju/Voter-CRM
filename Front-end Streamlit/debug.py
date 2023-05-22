import streamlit as st

def display_name(name):
    st.info(f'**Name:** {name}')
name = st.text_input('Please enter your name')

if not name:
    st.error("No name given")

if name:
    display_name(name)