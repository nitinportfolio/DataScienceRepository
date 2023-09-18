#from turtle import pd
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px




def main():
    st.title('Working With Plotly')
    
    df = pd.read_csv('cars.csv',index_col=0)
    
    st.dataframe(df)
    fig = px.pie(df,values = 'hp',names = df.index)
    st.plotly_chart(fig)
    
    fig2 = px.bar(df,x = 'hp',y = df.index)
    st.plotly_chart(fig2)






st.title(' Master  ❤️ ❤️ Dogu 🐕')
st.write(dir(st))

if __name__=='__main__':
    main()