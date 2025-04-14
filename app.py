#importacion de librerias.
import pandas as pd
import streamlit as st
import plotly.express as px

#lectura de datos
car_data = pd.read_csv('/Users/d.leon/Desktop/TRIPLETEN/proyecto-7/vehicles_us.csv') # leer los datos

#Encabezado de la app
st.header('ANALISIS DE VEHICULOS')

#Boton de histograma
if st.button("Mostrar histograma"):
    fig_histogram = px.histogram(car_data, x="odometer")  # ajusta la columna
    st.plotly_chart(fig_histogram, key='histograma')

#boton de grafico de dispersion
if st.button('Generar Gráfico de Dispersión'):
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Gráfico de Dispersión de Odómetro vs Precio")
    st.write(fig_scatter)
    st.plotly_chart(fig_scatter, key='dispersion')