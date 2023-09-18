from turtle import pd
import streamlit as st
import pandas as pd

from PIL import Image

# Text Input

fname = st.text_input('Enter First Name')
st.title(fname)
lname = st.text_input('Enter First Name', max_chars = 5)
st.title(lname)

# Hide Password
password = st.text_input('Enter Your Password',type = 'password')

# Text Area

message = st.text_area('Enter Your Feedback Here')
st.write(message)

bigmessage = st.text_area('Enter Message here', height = 200)
st.write(bigmessage)

# Enter Numbers
number1 = st.number_input('Please enter any number')

number2 = st.number_input('Please enter your age',1,100)


# Date Input
testdate = st.date_input(' Enter Test Date')

testtime =st.time_input(' Enter Test Time')

# Color Picker
color = st.color_picker('Select Color')

