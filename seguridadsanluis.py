import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Lista de diccionarios con la información de cada gráfico
info_graficos = [
    {'url': "https://www.datos.gov.co/resource/meew-mguv.csv?$query=SELECT%0A%20%20%60departamento%60%2C%0A%20%20%60municipio%60%2C%0A%20%20%60codigo_dane%60%2C%0A%20%20%60armas_medios%60%2C%0A%20%20%60fecha_hecho%60%2C%0A%20%20%60genero%60%2C%0A%20%20%60grupo_etario%60%2C%0A%20%20%60cantidad%60%0AWHERE%0A%20%20caseless_one_of(%60departamento%60%2C%20%22ANTIOQUIA%22)%0A%20%20AND%20caseless_one_of(%60municipio%60%2C%20%22SAN%20LUIS%22)", 'titulo': 'Amenazas en San Luis Antioquia por año', 'etiqueta_x': 'Año', 'etiqueta_y': 'Cantidad'},
    {'url': "https://www.datos.gov.co/resource/bz43-8ahq.csv?$query=SELECT%0A%20%20%60fecha_hecho%60%2C%0A%20%20%60cod_depto%60%2C%0A%20%20%60departamento%60%2C%0A%20%20%60cod_muni%60%2C%0A%20%20%60municipio%60%2C%0A%20%20%60zona%60%2C%0A%20%20%60sexo%60%2C%0A%20%20%60cantidad%60%0AWHERE%0A%20%20caseless_one_of(%60departamento%60%2C%20%22ANTIOQUIA%22)%0A%20%20AND%20caseless_one_of(%60municipio%60%2C%20%22SAN%20LUIS%22)%0AORDER%20BY%20%60fecha_hecho%60%20DESC%20NULL%20LAST", 'titulo': 'Delitos sexuales en San Luis Antioquia por año', 'etiqueta_x': 'Año', 'etiqueta_y': 'Cantidad'},
    # ... (repite el patrón para otros gráficos)
]

def crear_grafico(url, titulo, etiqueta_x, etiqueta_y):
    df = pd.read_csv(url)
    df['fecha_hecho'] = pd.to_datetime(df['fecha_hecho'])
    df['fecha_hecho'] = df['fecha_hecho'].dt.year
    cantidad_por_año = df['cantidad'].groupby(df['fecha_hecho']).sum()
    cantidad_por_año = cantidad_por_año.astype('int')
    cantidad_por_año.index = cantidad_por_año.index.astype('str')

    fig, ax = plt.subplots()
    ax.bar(cantidad_por_año.index, cantidad_por_año.values)
    ax.set_xlabel(etiqueta_x)
    ax.set_ylabel(etiqueta_y)
    ax.set_title(titulo)

    for i in range(len(cantidad_por_año)):
        ax.annotate(cantidad_por_año.values[i], (cantidad_por_año.index[i], cantidad_por_año.values[i]), ha='center', va='bottom')

    ax.set_xticks(cantidad_por_año.index)
    ax.set_xticklabels(cantidad_por_año.index, rotation=90)

    st.write(f"## {titulo}")
    st.pyplot(fig)

# Configuración de la página de Streamlit
st.title("SISTEMA DE INFORMACIÓN Y SEGURIDAD CIUDADANA DEL MUNICIPIO DE SAN LUIS ANTIOQUIA")

# Añadir gráficos uno por uno
for info in info_graficos:
    crear_grafico(info['url'], info['titulo'], info['etiqueta_x'], info['etiqueta_y'])


