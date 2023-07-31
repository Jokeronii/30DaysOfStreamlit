import streamlit as st

st.header("button streamlit")

if st.button('Say hello'):
    st.write("Hello bang ")
else :
    st.write("Goodbye bang ")