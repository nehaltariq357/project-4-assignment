import streamlit as st

st.title("Streamlit Fundamentals")

st.header("This is a Header")

st.subheader("This is SubHeader")

st.text("This is a Simple Text Output")

st.markdown("**This is bold text using markdown**")

name = "Nehal"
number = 10

st.write("Hello,", name)
st.write("This is a random number: ",number)

check =st.button("Click")
if check:
    st.text("Checkbox is checked")