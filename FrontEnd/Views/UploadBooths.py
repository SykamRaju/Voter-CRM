import pandas as pd
import streamlit as st
import os
from io import StringIO, BytesIO, FileIO
from typing import Callable
import json
from tempfile import NamedTemporaryFile
import pathlib
from API import API


class UploadBooths:
    def __init__(self, upload_polling_booths: Callable[[str], bool]):

        st.header("Upload Polling Booths")
        form = st.form("Upload_polling_booths")
        success: bool = False

        file = st.file_uploader("Please choose a CSV file.", type='csv')

        if file is not None:
            bytes_data  = file.read()


            with open(os.path.join("data/files",file.name),"wb") as f:
                f.write(file.getbuffer())

            file_to_upload = "data/files/"+file.name

            # try:
            if form.form_submit_button("Upload Voter Details"):
                # st.write(file_to_upload)
                file_details = {"file_name":file.name,"file_type":file.type,"file_size":file.size}
                result = upload_polling_booths(file_to_upload)
                st.success(result)


