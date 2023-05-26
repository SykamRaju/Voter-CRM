import streamlit as st
from typing import Callable


class AddConstituency:
    def __init__(self, on_submit: Callable[[str, str], bool]):
        st.header("Add New Constituency")

        form = st.form("new_constituency")
        constituency_name = form.text_input("Constituency name")
        # country = form.text_input("Country")

        if form.form_submit_button("Add New Constituency"):
            success = on_submit(constituency_name)
            if success:
                st.success("Constituency Added Successfully")
            else:
                st.error("Error adding Constituency")
