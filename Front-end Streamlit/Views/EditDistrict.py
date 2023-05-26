import streamlit as st
from typing import Callable


class EditDistrict:
    def __init__(self, get_distrits: Callable[[str], bool], on_submit2: Callable[[str], bool]):
        st.header("Edit District")
        districts=get_distrits()
        # st.write(states)
        district_names = [district["district_name"] for district in districts]
        form = st.form("edit_state")
        selected_district = form.selectbox("Select a District", district_names)
        district_name = form.text_input("New name for the District")

        if form.form_submit_button("Update State"):
            success = on_submit2(selected_district,district_name)
            if success:
                st.success("District Updated Successfully")
            else:
                st.error("Error updating District")
