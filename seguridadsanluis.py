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
    {'url': "https://www.datos.gov.co/resource/7i2x-h5vp.csv?$query=SELECT%0A%20%20%60fecha_hecho%60%2C%0A%20%20%60cod_depto%60%2C%0A%20%20%60departamento%60%2C%0A%20%20%60cod_muni%60%2C%0A%20%20%60municipio%60%2C%0A%20%20%60cantidad%60%0AWHERE%0A%20%20caseless_one_of(%60departamento%60%2C%20%22ANTIOQUIA%22)%0A%20%20AND%20caseless_one_of(%60municipio%60%2C%20%22SAN%20LUIS%22)%0AORDER%20BY%20%60fecha_hecho%60%20DESC%20NULL%20LAST", 'titulo': 'Hurtos al comercio en San Luis', 'etiqueta_x': 'Año', 'etiqueta_y': 'Cantidad'},
    {'url': "https://www.datos.gov.co/resource/4rxi-8m8d.csv?$query=SELECT%0A%20%20%60fecha_hecho%60%2C%0A%20%20%60cod_depto%60%2C%0A%20%20%60departamento%60%2C%0A%20%20%60cod_muni%60%2C%0A%20%20%60municipio%60%2C%0A%20%20%60cantidad%60%0AWHERE%0A%20%20caseless_one_of(%60departamento%60%2C%20%22ANTIOQUIA%22)%0A%20%20AND%20caseless_one_of(%60municipio%60%2C%20%22SAN%20LUIS%22)", 'titulo': 'Hurto a personas en San Luis', 'etiqueta_x': 'Año', 'etiqueta_y': 'Cantidad'},
    {'url': "https://www.datos.gov.co/resource/csb4-y6v2.csv?$query=SELECT%0A%20%20%60fecha_hecho%60%2C%0A%20%20%60cod_depto%60%2C%0A%20%20%60departamento%60%2C%0A%20%20%60cod_muni%60%2C%0A%20%20%60municipio%60%2C%0A%20%20%60tipo_delito%60%2C%0A%20%20%60zona%60%2C%0A%20%20%60cantidad%60%0AWHERE%0A%20%20caseless_one_of(%60departamento%60%2C%20%22ANTIOQUIA%22)%0A%20%20AND%20caseless_one_of(%60municipio%60%2C%20%22SAN%20LUIS%22)%0AORDER%20BY%20%60fecha_hecho%60%20DESC%20NULL%20LAST", 'titulo': 'Hurtos a residencias en San Luis', 'etiqueta_x': 'Año', 'etiqueta_y': 'Cantidad'},
    {'url': "https://www.datos.gov.co/resource/csb4-y6v2.csv?$query=SELECT%0A%20%20%60fecha_hecho%60%2C%0A%20%20%60cod_depto%60%2C%0A%20%20%60departamento%60%2C%0A%20%20%60cod_muni%60%2C%0A%20%20%60municipio%60%2C%0A%20%20%60tipo_delito%60%2C%0A%20%20%60zona%60%2C%0A%20%20%60cantidad%60%0AWHERE%0A%20%20caseless_one_of(%60departamento%60%2C%20%22ANTIOQUIA%22)%0A%20%20AND%20caseless_one_of(%60municipio%60%2C%20%22SAN%20LUIS%22)%0AORDER%20BY%20%60fecha_hecho%60%20DESC%20NULL%20LAST", 'titulo': 'Hurtos a vehículos en San Luis', 'etiqueta_x': 'Año', 'etiqueta_y': 'Cantidad'},
    {'url': "https://www.datos.gov.co/resource/ntej-qq7v.csv?$query=SELECT%0A%20%20%60fecha_hecho%60%2C%0A%20%20%60cod_depto%60%2C%0A%20%20%60departamento%60%2C%0A%20%20%60cod_muni%60%2C%0A%20%20%60municipio%60%2C%0A%20%20%60cantidad%60%0AWHERE%0A%20%20caseless_one_of(%60departamento%60%2C%20%22ANTIOQUIA%22)%0A%20%20AND%20caseless_one_of(%60municipio%60%2C%20%22SAN%20LUIS%22)%0AORDER%20BY%20%60fecha_hecho%60%20DESC%20NULL%20LAST", 'titulo': 'Lesiones accidente transito San Luis', 'etiqueta_x': 'Año', 'etiqueta_y': 'Cantidad'},
    {'url': "https://www.datos.gov.co/resource/jr6v-i33g.csv?$query=SELECT%0A%20%20%60fecha_hecho%60%2C%0A%20%20%60cod_depto%60%2C%0A%20%20%60departamento%60%2C%0A%20%20%60cod_muni%60%2C%0A%20%20%60municipio%60%2C%0A%20%20%60sexo%60%2C%0A%20%20%60cantidad%60%0AWHERE%0A%20%20caseless_one_of(%60departamento%60%2C%20%22ANTIOQUIA%22)%0A%20%20AND%20caseless_one_of(%60municipio%60%2C%20%22SAN%20LUIS%22)%0AORDER%20BY%20%60fecha_hecho%60%20DESC%20NULL%20LAST", 'titulo': 'Lesiones personales en San Luis', 'etiqueta_x': 'Año', 'etiqueta_y': 'Cantidad'},
    {'url': "https://www.datos.gov.co/resource/sutf-7dyz.csv?$query=SELECT%0A%20%20%60fecha_hecho%60%2C%0A%20%20%60cod_depto%60%2C%0A%20%20%60departamento%60%2C%0A%20%20%60cod_muni%60%2C%0A%20%20%60municipio%60%2C%0A%20%20%60zona%60%2C%0A%20%20%60cantidad%60%0AWHERE%0A%20%20caseless_one_of(%60departamento%60%2C%20%22ANTIOQUIA%22)%0A%20%20AND%20caseless_one_of(%60municipio%60%2C%20%22SAN%20LUIS%22)", 'titulo': 'Piratería terrestre en San Luis', 'etiqueta_x': 'Año', 'etiqueta_y': 'Cantidad'},
    {'url': "https://www.datos.gov.co/resource/m8fd-ahd9.csv?$query=SELECT%0A%20%20%60fecha_hecho%60%2C%0A%20%20%60cod_depto%60%2C%0A%20%20%60departamento%60%2C%0A%20%20%60cod_muni%60%2C%0A%20%20%60municipio%60%2C%0A%20%20%60zona%60%2C%0A%20%20%60sexo%60%2C%0A%20%20%60cantidad%60%0AWHERE%0A%20%20caseless_one_of(%60departamento%60%2C%20%22ANTIOQUIA%22)%0A%20%20AND%20caseless_one_of(%60municipio%60%2C%20%22SAN%20LUIS%22)", 'titulo': 'Homicidios en San Luis', 'etiqueta_x': 'Año', 'etiqueta_y': 'Cantidad'},
    {'url': "https://www.datos.gov.co/resource/d7zw-hpf4.csv?$query=SELECT%0A%20%20%60fecha_hecho%60%2C%0A%20%20%60cod_depto%60%2C%0A%20%20%60departamento%60%2C%0A%20%20%60cod_muni%60%2C%0A%20%20%60municipio%60%2C%0A%20%20%60tipo_delito%60%2C%0A%20%20%60cantidad%60%0AWHERE%0A%20%20caseless_one_of(%60departamento%60%2C%20%22ANTIOQUIA%22)%0A%20%20AND%20caseless_one_of(%60municipio%60%2C%20%22SAN%20LUIS%22)%0AORDER%20BY%20%60fecha_hecho%60%20DESC%20NULL%20LAST", 'titulo': 'Secuestros en San Luis', 'etiqueta_x': 'Año', 'etiqueta_y': 'Cantidad'},
    {'url': "https://www.datos.gov.co/resource/gepp-dxcs.csv?$query=SELECT%0A%20%20%60fecha_hecho%60%2C%0A%20%20%60cod_depto%60%2C%0A%20%20%60departamento%60%2C%0A%20%20%60cod_muni%60%2C%0A%20%20%60municipio%60%2C%0A%20%20%60zona%60%2C%0A%20%20%60cantidad%60%0AWHERE%0A%20%20caseless_one_of(%60departamento%60%2C%20%22ANTIOQUIA%22)%0A%20%20AND%20caseless_one_of(%60municipio%60%2C%20%22SAN%20LUIS%22)%0AORDER%20BY%20%60fecha_hecho%60%20DESC%20NULL%20LAST", 'titulo': 'Violencia intrafamiliar en San Luis', 'etiqueta_x': 'Año', 'etiqueta_y': 'Cantidad'},

    # ... (repite el patrón para otros gráficos)
]

# Configuración de la página de Streamlit
st.title("SISTEMA DE INFORMACIÓN Y SEGURIDAD CIUDADANA DEL MUNICIPIO DE SAN LUIS ANTIOQUIA")

# Definir el diseño de la cuadrícula (2 columnas)
num_columnas = 2

# Calcular el número de filas necesarias
num_filas = len(info_graficos) // num_columnas
if len(info_graficos) % num_columnas != 0:
    num_filas += 1

# Añadir gráficos en una cuadrícula
for i in range(num_filas):
    col1, col2 = st.columns(num_columnas)
    for j in range(num_columnas):
        index = i * num_columnas + j
        if index < len(info_graficos):
            info = info_graficos[index]
            crear_grafico(info, col1 if j == 0 else col2)










