from turtle import pd
import streamlit as st
import pandas as pd

from PIL import Image
img = Image.open('dog01.jpg')

# st.set_page_config(page_title='Hello Nitin',
#                  page_icon = ':smiley:')

st.set_page_config(page_title='Hello Nitin',
                   page_icon = img,
                   layout = 'wide',
                   initial_sidebar_state = 'auto')
                   
# 'expanded')
# 'collapsed')



st.title(' Hello Nitin Wolcome to StreamLit ❤️ ❤️')
st.sidebar.success('Menu')