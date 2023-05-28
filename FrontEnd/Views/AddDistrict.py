import streamlit as st
from typing import Callable


class AddDistrict:
    def __init__(self,get_states: Callable[[str], bool], on_submit: Callable[[str, str], bool]):
        st.header("Add New District")
        states=get_states()
        state_names = [state["state_name"] for state in states]
        form = st.form("new_district")
        selected_state = form.selectbox("Select a state", state_names)
        district_name = form.text_input("District name")

        if form.form_submit_button("Add New District"):
            success = on_submit(selected_state,district_name)
            if success:
                st.success("District Added Successfully")
            else:
                st.error("Error adding District")
