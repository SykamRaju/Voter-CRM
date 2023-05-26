import streamlit as st
from typing import Callable


class DeleteDistrict:
    def __init__(self, get_states: Callable[[str], bool], delete: Callable[[str], bool]):
        st.header("Delete State")
        states=get_states()
        state_names = [state["state_name"] for state in states]
        form = st.form("delete_state")
        selected_state = form.selectbox("Select a state", state_names)

        if form.form_submit_button("Delete State"):
            success = delete(selected_state)
            if success:
                st.success("State deleted Successfully")
            else:
                st.error("Error deleting state")
