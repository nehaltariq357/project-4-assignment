import streamlit as st
import pandas as pd

data = {
    "Name":["John","Anna","Peter","Linda"],
    "age":[23,29,35,32],
    "City":["NewYork","Paris","Berlin","London"]
}

df = pd.DataFrame(data)

city = st.selectbox("Choose a city to filter", df["City"].unique())
filtered_data = df[df["City"]==city]

st.write(f"Data for city: {city}")
st.dataframe(filtered_data)