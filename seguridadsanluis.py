import streamlit as st
import pandas as pd

def crear_grafico(url, titulo, etiqueta_x, etiqueta_y):
    st.write(f"## {titulo}")
    df = pd.read_csv(url)
    df['fecha_hecho'] = pd.to_datetime(df['fecha_hecho'])
    df['fecha_hecho'] = df['fecha_hecho'].dt.year
    cantidad_por_año = df['cantidad'].groupby(df['fecha_hecho']).sum()
    cantidad_por_año = cantidad_por_año.astype('int')
    cantidad_por_año.index = cantidad_por_año.index.astype('str')

    st.bar_chart(cantidad_por_año, use_container_width=True)

    st.xlabel(etiqueta_x)
    st.ylabel(etiqueta_y)

# Configurar la página de Streamlit
st.set_page_config(page_title="SISTEMA DE INFORMACIÓN Y SEGURIDAD CIUDADANA", page_icon=":chart_with_upwards_trend:")

# Añadir líneas de texto personalizadas
st.title("MUNICIPIO DE SAN LUIS")
st.write("SISTEMA DE INFORMACIÓN Y SEGURIDAD CIUDADANA")

# URLs específicas para cada gráfico
info_graficos = [
    {'url': "https://www.datos.gov.co/resource/meew-mguv.csv?$query=SELECT%0A%20%20%60departamento%60%2C%0A%20%20%60municipio%60%2C%0A%20%20%60codigo_dane%60%2C%0A%20%20%60armas_medios%60%2C%0A%20%20%60fecha_hecho%60%2C%0A%20%20%60genero%60%2C%0A%20%20%60grupo_etario%60%2C%0A%20%20%60cantidad%60%0AWHERE%0A%20%20caseless_one_of(%60departamento%60%2C%20%22ANTIOQUIA%22)%0A%20%20AND%20caseless_one_of(%60municipio%60%2C%20%22SAN%20LUIS%22)",
     'titulo': 'Amenazas en San Luis Antioquia por año', 'etiqueta_x': 'Año', 'etiqueta_y': 'Cantidad'},
    # ... Repite esto para los demás gráficos
]

# Mostrar los gráficos con Streamlit
for info in info_graficos:
    crear_grafico(info['url'], info['titulo'], info['etiqueta_x'], info['etiqueta_y'])

# Agregar nota en la parte inferior
st.text("Creado por John Alexander Echeverry Ocampo, politólogo y analista de datos")




