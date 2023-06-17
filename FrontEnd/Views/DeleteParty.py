import streamlit as st
from typing import Callable


class DeleteParty:
    def __init__(self, get_parties: Callable[[str], bool], delete: Callable[[str], bool]):
        st.header("Delete Political Parties")
        parties=get_parties()
        if parties is not None:
            party_names = [party["Party_Name"] for party in parties]
            form = st.form("delete_party")
            selected_party = form.selectbox("Select a party", party_names)

            if form.form_submit_button("Delete Party"):
                success = delete(selected_party)
                if success:
                    st.success("Party deleted Successfully")
                else:
                    st.error("Error deleting Party")
        else:
            st.error("Political Parties Record is empty!")
