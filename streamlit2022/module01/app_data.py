from turtle import pd
import streamlit as st
import pandas as pd

# Dispalying data

df = pd.read_csv('cars.csv')

# Method 01
st.dataframe(df)

# Giving Height & Width

st.dataframe(df, 500,200)

# Getting Name of Columns
st.dataframe(df.columns)

# Other statistics
st.dataframe(df.style.highlight_max(axis=0))

# Using Super Function
st.header('Head')
st.write(df.head())

# Static Data
st.table(df)

# JSON
st.header('JSON')
st.json({'data':'Nitin'})

# Display Code
st.header('Code')
mycode = """
def myfunc():
    print("Hello World!!!")
"""
st.code(mycode, language = 'ruby')

st.code(mycode, language = 'python')







