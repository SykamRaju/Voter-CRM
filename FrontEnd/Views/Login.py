import streamlit as st
from typing import Callable
import extra_streamlit_components as stx

class Login:
    def __init__(self,on_login:Callable[[str,str],bool]):
        self.on_login = on_login
        st.header("Login")
        self.username=st.text_input("Username")
        self.password=st.text_input("Password",type="password")

        st.button("Login", on_click=self.LogIn_Clicked)
        
            
    
    def LogIn_Clicked(self):
        success = self.on_login(self.username, self.password)
        if success:
            st.write("Login Successful")
            st.stop()
            # st.success("Welcome, logged-in user!")
        else:
            st.error("Incorrect Username and password combination")
            st.stop()
