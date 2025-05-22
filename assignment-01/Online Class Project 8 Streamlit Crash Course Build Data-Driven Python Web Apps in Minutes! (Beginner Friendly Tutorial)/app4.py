import streamlit as st

#use what you are learned to create a simple app that asks for user input (name, age, fav number) and dynamically displays the result


st.title("User Input Form")

name = st.text_input("Enter your name")
age = st.slider("select your age",0,100)
fav_number = st.number_input("Enter your favourite number",0,100)
if st.button("Click"):
    st.write(f"Hello, {name}!, you are {age} year old, your favourite number is {fav_number}")