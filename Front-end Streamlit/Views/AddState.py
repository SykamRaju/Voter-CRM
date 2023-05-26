import streamlit as st
from typing import Callable


class AddState:
    def __init__(self, on_submit: Callable[[str, str], bool]):
        st.header("Add New State")

        form = st.form("new_state")
        state_name = form.text_input("State name")
        # country = form.text_input("Country")

        if form.form_submit_button("Add New State"):
            success = on_submit(state_name)
            if success:
                st.success("State Added Successfully")
            else:
                st.error("Error adding state")
