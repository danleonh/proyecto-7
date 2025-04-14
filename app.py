import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('/Users/d.leon/Desktop/TRIPLETEN/proyecto-7/vehicles_us.csv') # leer los datos

st.header('ANALISIS DE VEHICULOS')

