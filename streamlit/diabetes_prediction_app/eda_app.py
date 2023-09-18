import streamlit as st

# Load EDA libraries
import pandas as pd
import numpy as np

# Load Viz Libraries
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import plotly.express as px

# Load Data
@st.cache
def load_data(data):
    df = pd.read_csv(data)
    return (df)

def run_eda_app():
    st.subheader('From Exploratory Data Analysis')
    data = load_data("data/diabetes_data.csv")
    data_encoder = load_data('data/diabetes_data_clean.csv')
    #st.dataframe(data)

    submenu = st.sidebar.selectbox('submenu',['Descriptive','Plots'])

    if submenu == 'Descriptive':
        st.dataframe(data)

        with st.expander('Data Shape'):
            st.dataframe(pd.DataFrame(data.shape,  columns = ['Count'],index=['Rows','Columns']).astype(str))

        with st.expander('Data Types'):
            st.dataframe(pd.DataFrame(data.dtypes,  columns = ['Dtypes']).astype(str))

        with st.expander('Descriptive Summary'):
            st.dataframe((data_encoder.describe()).astype(str))

        with st.expander('Class Distribution'):
            st.dataframe(data['class'].value_counts())

        with st.expander('Gender Distribution'):
            st.dataframe(data['Gender'].value_counts())

        with st.expander('Value Counts For All Columns'):
            for i in data.columns:
                st.write(i)
                st.write(data[i].value_counts())
                st.write('----')

    elif submenu == 'Plots':

        pass
