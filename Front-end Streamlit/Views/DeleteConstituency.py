import streamlit as st
from typing import Callable


class DeleteConstituency:
    def __init__(self, get_districts: Callable[[str], bool], delete: Callable[[str], bool]):
        st.header("Delete Constituency")
        districts=get_districts()
        district_names = [district["district_name"] for district in districts]
        form = st.form("delete_constituency")
        selected_constituency = form.selectbox("Select a Constituency", district_names)

        if form.form_submit_button("Delete State"):
            success = delete(selected_constituency)
            if success:
                st.success("Constituency deleted Successfully")
            else:
                st.error("Error deleting Constituency")
