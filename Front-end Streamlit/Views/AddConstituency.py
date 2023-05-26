import streamlit as st
from typing import Callable


class AddConstituency:
    def __init__(self,get_districts: Callable[[str], bool], on_submit: Callable[[str, str], bool]):
        st.header("Add New Constituency")
        districts=get_districts()
        district_names = [district["district_name"] for district in districts]
        form = st.form("new_constituency")
        selected_district = form.selectbox("Select a District", district_names)
        constituency_name = form.text_input("Constituency name")

        if form.form_submit_button("Add New Constituency"):
            success = on_submit(selected_district,constituency_name)
            if success:
                st.success("Constituency Added Successfully")
            else:
                st.error("Error adding Constituency")