import streamlit as st 

col1, col2, col3 = st.columns(3)

col1.title("Upload your files ")

x=col1.file_uploader("Upload your documents ")
