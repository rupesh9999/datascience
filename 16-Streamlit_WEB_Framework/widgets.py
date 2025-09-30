import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name=st.text_input("Enter your name:")

age=st.slider("select your age:",1,100,25)

st.write("Your age is {age}.")

options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Select your favorite programming language:", options)
st.write("You selected {choice}.")

if name:
    st.write(f"Hello ",{name})

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "San Francisco", "Los Angeles"]

}

df = pd.DataFrame(data)
st.write(df)

uploaded_file= st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)