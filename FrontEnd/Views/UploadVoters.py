import pandas as pd
import streamlit as st
import os
from io import StringIO, BytesIO, FileIO
from typing import Callable
import json
import pathlib
from API import API


class UploadVoters:
    def __init__(self, upload_voters: Callable[[str], bool]):

        st.header("Upload Voters")
        form = st.form("Upload_voters")
        success: bool = False

        voter_file = st.file_uploader("Please choose a CSV file.", type='csv',key="upload_voters")

        if voter_file is not None:
            bytes_data  = voter_file.read()


            with open(os.path.join("data/files",voter_file.name),"wb") as f:
                f.write(voter_file.getbuffer())

            file_to_upload = "data/files/"+voter_file.name

            # try:
            if form.form_submit_button("Upload Voter Details"):
                with st.spinner('Processing the submitted file ...'):
                    # st.write(file_to_upload)
                    file_details = {"file_name":voter_file.name,"file_type":voter_file.type,"file_size":voter_file.size}
                    result = upload_voters(file_to_upload)
                    st.success(result)
                


