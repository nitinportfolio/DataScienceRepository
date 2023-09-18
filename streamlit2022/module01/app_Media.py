from turtle import pd
import streamlit as st
import pandas as pd

from PIL import Image

# Working with Media Files - Images/ Vidoes/ Audio

# Image
img = Image.open('dog01.jpg')
st.image(img)

img2 = Image.open('dog02.jpeg')
st.image(img2, use_column_width = True)


img3 = Image.open('porsche.jpg')
st.image(img3, use_column_width = True)

st.image("https://cdp.azureedge.net/products/USA/HD/2021/MC/SPORTSTER/SPORTSTER_S/50/VIVID_BLACK/2000000001.jpg")

# Rading Audio Files
audio_file = open('harley-audio.mp3','rb')
st.audio(audio_file.read())


# Reading Video Files

vid_file = open('harley-video.mp4','rb').read()
st.video(vid_file, start_time = 2)


st.video(open('Star.mp4','rb').read())

with open('harley-video.mp4', 'rb') as vid:
    st.video(vid)