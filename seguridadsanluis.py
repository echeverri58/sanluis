import streamlit as st
import pandas as pd
import altair as alt

# Lista de diccionarios con la información de cada gráfico
info_graficos = [
    {'url': "https://www.datos.gov.co/resource/meew-mguv.csv?$query=SELECT%0A%20%20%60departamento%60%2C%0A%20%20%60municipio%60%2C%0A%20%20%60codigo_dane%60%2C%0A%20%20%60armas_medios%60%2C%0A%20%20%60fecha_hecho%60%2C%0A%20%20%60genero%60%2C%0A%20%20%60grupo_etario%60%2C%0A%20%20%60cantidad%60%0AWHERE%0A%20%20caseless_one_of(%60departamento%60%2C%20%22ANTIOQUIA%22)%0A%20%20AND%20caseless_one_of(%60municipio%60%2C%20%22SAN%20LUIS%22)", 'titulo': 'Amenazas en San Luis Antioquia por año', 'etiqueta_x': 'Año', 'etiqueta_y': 'Cantidad'},
    {'url': "https://www.datos.gov.co/resource/bz43-8ahq.csv?$query=SELECT%0A%20%20%60fecha_hecho%60%2C%0A%20%20%60cod_depto%60%2C%0A%20%20%60departamento%60%2C%0A%20%20%60cod_muni%60%2C%0A%20%20%60municipio%60%2C%0A%20%20%60zona%60%2C%0A%20%20%60sexo%60%2C%0A%20%20%60cantidad%60%0AWHERE%0A%20%20caseless_one_of(%60departamento%60%2C%20%22ANTIOQUIA%22)%0A%20%20AND%20caseless_one_of(%60municipio%60%2C%20%22SAN%20LUIS%22)%0AORDER%20BY%20%60fecha_hecho%60%20DESC%20NULL%20LAST", 'titulo': 'Delitos sexuales en San Luis Antioquia por año', 'etiqueta_x': 'Año', 'etiqueta_y': 'Cantidad'},
    {'url': "https://www.datos.gov.co/resource/meew-mguv.csv?$query=SELECT%0A%20%20%60departamento%60%2C%0A%20%20%60municipio%60%2C%0A%20%20%60codigo_dane%60%2C%0A%20%20%60armas_medios%60%2C%0A%20%20%60fecha_hecho%60%2C%0A%20%20%60genero%60%2C%0A%20%20%60grupo_etario%60%2C%0A%20%20%60cantidad%60%0AWHERE%0A%20%20caseless_one_of(%60departamento%60%2C%20%22ANTIOQUIA%22)%0A%20%20AND%20caseless_one_of(%60municipio%60%2C%20%22SAN%20LUIS%22)", 'titulo': 'Amenazas en San Luis Antioquia por año', 'etiqueta_x': 'Año', 'etiqueta_y': 'Cantidad'},
    {'url': "https://www.datos.gov.co/resource/bz43-8ahq.csv?$query=SELECT%0A%20%20%60fecha_hecho%60%2C%0A%20%20%60cod_depto%60%2C%0A%20%20%60departamento%60%2C%0A%20%20%60cod_muni%60%2C%0A%20%20%60municipio%60%2C%0A%20%20%60zona%60%2C%0A%20%20%60sexo%60%2C%0A%20%20%60cantidad%60%0AWHERE%0A%20%20caseless_one_of(%60departamento%60%2C%20%22ANTIOQUIA%22)%0A%20%20AND%20caseless_one_of(%60municipio%60%2C%20%22SAN%20LUIS%22)%0AORDER%20BY%20%60fecha_hecho%60%20DESC%20NULL%20LAST", 'titulo': 'Delitos sexuales en San Luis Antioquia por año', 'etiqueta_x': 'Año', 'etiqueta_y': 'Cantidad'},
    {'url': "https://www.datos.gov.co/resource/q2ib-t9am.csv?$query=SELECT%0A%20%20%60fecha_hecho%60%2C%0A%20%20%60cod_depto%60%2C%0A%20%20%60departamento%60%2C%0A%20%20%60cod_muni%60%2C%0A%20%20%60municipio%60%2C%0A%20%20%60cantidad%60%0AWHERE%0A%20%20caseless_one_of(%60departamento%60%2C%20%22ANTIOQUIA%22)%0A%20%20AND%20caseless_one_of(%60municipio%60%2C%20%22SAN%20LUIS%22)%0AORDER%20BY%20%60fecha_hecho%60%20DESC%20NULL%20LAST", 'titulo': 'Extorsión en San Luis Antioquia por año', 'etiqueta_x': 'Año', 'etiqueta_y': 'Cantidad'},
    # Agregar las otras 10 URLs aquí
]

# Función para crear gráfico a partir de la URL
def crear_grafico(url, titulo, etiqueta_x, etiqueta_y):
    df = pd.read_csv(url)
    chart = alt.Chart(df).mark_bar().encode(
        x=etiqueta_x,
        y=etiqueta_y,
        tooltip=['fecha_hecho', alt.Tooltip('cantidad', title='Cantidad')],
    ).properties(
        title=titulo
    )
    return chart

# Configuración de la página de Streamlit
st.title("Visualización de Datos")

# Añadir gráficos en filas
for info in info_graficos:
    # Crear el



