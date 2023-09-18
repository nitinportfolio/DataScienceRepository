from turtle import pd
import streamlit as st
import pandas as pd

from PIL import Image
img = Image.open('dog01.jpg')


# Method 01
# st.set_page_config(page_title='Hello Nitin',
#                  page_icon = ':smiley:')

#st.set_page_config(page_title='Hello Nitin',
#                   page_icon = img,
 #                  layout = 'wide',
#                 initial_sidebar_state = 'auto')
#*/                   
# 'expanded')
# 'collapsed')

# Dictionary Method 02

PAGE_CONFIG = {'page_title':'Hellow World',
               'page_icon':':smiley:',
               'layout':'wide'}
st.set_page_config(**PAGE_CONFIG)





st.title(' Hello Nitin Wolcome to StreamLit ❤️ ❤️')
st.sidebar.success('Menu')