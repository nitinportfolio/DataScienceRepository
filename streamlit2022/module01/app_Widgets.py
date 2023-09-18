from turtle import pd
import streamlit as st
import pandas as pd

# Dispalying Buttons

st.button('Submitt')
name = 'Nitin'

if st.button('Submit'):
    
    st.header('Hello') 
    st.write("Mr : {}".format(name.upper()))
    
if st.button('Submit', key = 'sub02'):
    st.title('Hello World!!')
    
# Working With Radio Buttons

status = st.radio('What is your status',('Active','Inactive'))

status1 = st.radio(' Please choose your option',('Active','Inactive'))

if status1 =='Active':
    st.success('You are Passes Hey!!')
else:
    st.error('You are Failed')
    
    
# Working With CheckBox
if st.checkbox('Show/Hide'):
    st.text('Showing Something')
    
    
# WOrking with Beta Expander
if st.expander('Python'):
    st.success('Hello World')
    
with st.expander('Nitin'):
    st.text('Hi Nitin')
    
    
# Working With Select & Multi Select Options
my_lang = ['Python','Julia','Java','Go','Ruby']

choice = st.selectbox('Language',my_lang)
st.write('You Selected {}'.format(choice))

# multi Select

spoken_lang = ['Hindi','Sanskrit','English','French']
my_spoken_lang = st.multiselect('I Speak', spoken_lang)
my_spoken_lang = st.multiselect('I Speak', spoken_lang, default = 'Hindi')


# WOrking With Slider
# Numbers- - Int /Float/Date
age = st.slider('Age',1,100)

# Slider With Range
age = st.slider('New Age',1,100,5)

# Select Slider 
# Any Datatype
colors = st.select_slider(
    'Choose Color',
    options = ['red','green','blue','yellow','black'],
    value = ['red','yellow']
)








