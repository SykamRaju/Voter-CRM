import streamlit as st
from typing import Callable

class Login:
    def __init__(self,on_login:Callable[[str,str],bool],on_signup: Callable[[str,str],bool]):
        st.title("VoterCRM")
        options= ['Login', 'Sign Up']
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row; justify-content: space-around;}</style>', unsafe_allow_html=True)
        option = st.radio('options', options, horizontal=True, label_visibility='hidden')
                
        if option == 'Login':
            self.Display_Login(on_login)
        else:
            self.Display_Signup(on_signup)

    def Display_Login(self, on_login:Callable[[str,str],bool]):
        self.on_login = on_login
        st.header("Login")
        self.username=st.text_input("Username", key='login_username')
        self.password=st.text_input("Password",type="password", key='login_password')

        col1, _col2, col3 = st.columns([0.2, 0.8, 0.27])
        with col1:
            st.button("Login", on_click=self.LogIn_Clicked)
        with col3:
            st.button("Forgot Password", on_click=self.Fetch_Password(self.username))

    def Display_Signup(self, on_signup:Callable[[str,str],bool]):
        self.on_signup = on_signup
        st.header("Sign Up")
        self.sign_username=st.text_input("Username", key='sign_username')
        self.sign_password=st.text_input("Password",type="password", key='sign_password')
        self.sign_confirm_password=st.text_input("Confirm Password",type="password")
        if st.button("Sign Up"):
            self.SignUp_Clicked()


    def LogIn_Clicked(self):
        success = self.on_login(self.username, self.password)
        if success:
            st.write("Login Successful")
            st.stop()
            # st.success("Welcome, logged-in user!")
        else:
            st.error("Incorrect Username and password combination")
            st.stop()

    def SignUp_Clicked(self):
        success = self.on_signup(self.sign_username, self.sign_password)
        if success:
            st.write("Sign up Successful")
            st.stop()
            # st.success("Welcome, logged-in user!")
        else:
            st.error("Sign up Failed! Please try again")
            st.stop()

    def Fetch_Password(self, username):
        pass
