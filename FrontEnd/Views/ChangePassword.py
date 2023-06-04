import streamlit as st
from typing import Callable

class ChangePassword:
    def __init__(self, on_change_password: Callable[[object], bool]):
        self.on_change_password = on_change_password
        st.header("Change Password")
        self.username = st.text_input("Username", key='cp_username')
        self.old_password = st.text_input(
            "Current Password", type="password", key='cp_old_password')
        self.new_password = st.text_input(
            "New Password", type="password", key='cp_new_password')
        self.retype_new_password = st.text_input(
            "Retype New Password", type="password", key='cp_rnew_password')
        if st.button('Change Password'):
            self.change_psswrd_details = {
            "Username": self.username,
            "Old_Password": self.old_password,
            "New_Password": self.new_password,
            "Retype_New_Password": self.retype_new_password
        }
            self.Change_Password(self.change_psswrd_details)

    def Change_Password(self, psswrd_details):
        success = self.on_change_password(psswrd_details)
        if success:
            st.success("Password Changed Successfully!.")
        else:
            st.error("An Error occurred! Please check for password consistency and try again.")
