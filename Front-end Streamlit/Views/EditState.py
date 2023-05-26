import streamlit as st
from typing import Callable


class EditState:
    def __init__(self, get_states: Callable[[str], bool], on_submit2: Callable[[str], bool]):
        st.header("Edit State")
        states=get_states()
        # st.write(states)
        state_names = [state["state_name"] for state in states]
        form = st.form("edit_state")
        selected_state = form.selectbox("Select a state", state_names)
        state_name = form.text_input("New name for the State")
        # country = form.text_input("Country")

        if form.form_submit_button("Update State"):
            success = on_submit2(state_name)
            if success:
                st.success("State Updated Successfully")
            else:
                st.error("Error updating state")
