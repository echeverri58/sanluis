import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

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

    st.pyplot(fig)

# Configuración de la página de Streamlit
st.title("SISTEMA DE INFORMACIÓN Y SEGURIDAD CIUDADANA DEL MUNICIPIO DE SAN LUIS ANTIOQUIA")

# Añadir gráficos uno por uno
for info in info_graficos:
    st.subheader(info['titulo'])
    crear_grafico(info['url'], info['titulo'], info['etiqueta_x'], info['etiqueta_y'])

