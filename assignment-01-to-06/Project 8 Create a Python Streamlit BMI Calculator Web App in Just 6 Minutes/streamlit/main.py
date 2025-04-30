
import streamlit as st

st.title("BMI Calculator")
height = st.slider("Enter your height (in cm):",100,250,175)# start,end,default
weight = st.slider("Enter your weight (in kg):",40,200,70)# start,end,default

bmi = weight / ((height/100)**2)

st.write(f"Your BMI is {bmi:.2f}")

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <=bmi< 24.9:
    category = "Normal weight"
elif 25 <=bmi<29.9:
    category = "Overweight"
else:
    category = "Obesity"

st.write(f"Category: **{category}**")

st.write("### BMI Categories ###")
st.write("-Underweight: BMI less than 18.5")
st.write("-Normal weight: BMI between 18.5 and 24.9")
st.write("-Overweight: BMI between 25 and 29.9")
st.write("-Obesity: BMI 30 or greater")