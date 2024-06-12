import streamlit as st
import pandas as pd
import numpy as np
import pymupdf as pymupdf

st.title('Hi! Welcome to the PDF Cat Reader.')

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf", accept_multiple_files=False)



if uploaded_file is not None:
    #process_pdf(uploaded_file)
    doc = pymupdf.open(uploaded_file)