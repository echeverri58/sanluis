import streamlit as st
import pandas as pd
import altair as alt

# URL con los datos
url = "https://www.datos.gov.co/resource/meew-mguv.csv?$query=SELECT%0A%20%20%60departamento%60%2C%0A%20%20%60municipio%60%2C%0A%20%20%60codigo_dane%60%2C%0A%20%20%60armas_medios%60%2C%0A%20%20%60fecha_hecho%60%2C%0A%20%20%60genero%60%2C%0A%20%20%60grupo_etario%60%2C%0A%20%20%60cantidad%60%0AWHERE%0A%20%20caseless_one_of(%60departamento%60%2C%20%22ANTIOQUIA%22)%0A%20%20AND%20caseless_one_of(%60municipio%60%2C%20%22SAN%20LUIS%22)"

# Título y descripción de la aplicación
st.title("Visualización de Datos - San Luis Antioquia")
st.write("A continuación se presenta un gráfico interactivo sobre amenazas en San Luis Antioquia por año.")

# Cargar datos desde la URL
df = pd.read_csv(url)
df['fecha_hecho'] = pd.to_datetime(df['fecha_hecho'])
df['año'] = df['fecha_hecho'].dt.year

# Crear gráfico interactivo con Altair
chart = alt.Chart(df).mark_bar().encode(
    x='año:O',
    y='sum(cantidad):Q',
    color='genero:N',
    tooltip=['año:O', 'sum(cantidad):Q']
).properties(
    width=600,
    title='Amenazas en San Luis Antioquia por año'
)

# Mostrar gráfico en Streamlit
st.altair_chart(chart, use_container_width=True)






