#importacion de librerias.
import pandas as pd
import streamlit as st
import plotly.express as px

#lectura de datos
car_data = pd.read_csv('/Users/d.leon/Desktop/TRIPLETEN/proyecto-7/vehicles_us.csv') # leer los datos

#Encabezado de la app
st.header('ANALISIS DE VEHICULOS')

if st.button("Mostrar histograma"):
    fig = px.histogram(car_data, x="odometer")  # ajusta la columna
    st.plotly_chart(fig)

