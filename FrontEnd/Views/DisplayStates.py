import streamlit as st
from typing import Callable

class DisplayStates:
    def __init__(self,get_states:Callable[[],list]):
        st.header("List of States")
        states=get_states()
        if states is None:
            st.error("States Record is empty!")
        else:
            st.table(states)      