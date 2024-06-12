import streamlit as st
import pandas as pd
import numpy as np
import pymupdf as pymupdf

st.title('Hi! Welcome to the PDF Cat Reader.')

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf", accept_multiple_files=False)

if uploaded_file is not None:
    doc = pymupdf.open(stream=uploaded_file.read(), filetype="pdf")

    words_count = 0
    for page in doc:
        words_count += len(page.get_text().split())

    st.write(f"Total words in the PDF: {words_count}")