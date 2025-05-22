import streamlit as st


name = st.text_input("Enter your name")
age = st.slider("Select your age",0,100)

if st.button("Submit"):
    st.write(f"Hello **{name}**, you are **{age}** year old")