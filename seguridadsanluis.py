import pandas as pd
import streamlit as st
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.palettes import Spectral11
from bokeh.embed import components

def crear_grafico(url, titulo, color):
    try:
        df = pd.read_csv(url)
        if df.empty:
            st.warning(f"No hay datos para el gráfico: {titulo}")
            return None
        df['fecha_hecho'] = pd.to_datetime(df['fecha_hecho'], errors='coerce')
        df = df.dropna(subset=['fecha_hecho'])
        df['año'] = df['fecha_hecho'].dt.year
        cantidad_por_año = df.groupby('año')['cantidad'].sum().astype(int)
        años = sorted(cantidad_por_año.index.astype(str))

        if len(años) == 0:
            st.warning(f"No hay datos válidos para el gráfico: {titulo}")
            return None

        source = ColumnDataSource(data=dict(
            year=años,
            cantidad=cantidad_por_año.values
        ))

        p = figure(title=titulo, x_range=años, height=300, width=500, toolbar_location=None, tools="")

        p.vbar(x='year', top='cantidad', width=0.9, source=source, line_color='white', fill_color=color)

        p.xgrid.grid_line_color = None
        p.y_range.start = 0
        p.xaxis.axis_label = 'Año'
        p.yaxis.axis_label = 'Cantidad'
        p.axis.minor_tick_line_color = None
        p.outline_line_color = None

        p.xaxis.major_label_orientation = -3.14 / 2  # -90 grados

        hover = HoverTool(tooltips=[('Año', '@year'), ('Cantidad', '@cantidad')])
        p.add_tools(hover)

        return p
    except Exception as e:
        st.error(f"Error al crear el gráfico {titulo}: {str(e)}")
        return None

# Ejemplo de URLs y títulos
info_graficos = [
    {'url': "https://www.datos.gov.co/resource/meew-mguv.csv?$query=SELECT%0A%20%20%60departamento%60%2C%0A%20%20%60municipio%60%2C%0A%20%20%60codigo_dane%60%2C%0A%20%20%60armas_medios%60%2C%0A%20%20%60fecha_hecho%60%2C%0A%20%20%60genero%60%2C%0A%20%20%60grupo_etario%60%2C%0A%20%20%60cantidad%60%0AWHERE%0A%20%20caseless_one_of(%60departamento%60%2C%20%22ANTIOQUIA%22)%0A%20%20AND%20caseless_one_of(%60municipio%60%2C%20%22SAN%20LUIS%22)", 'titulo': 'Amenazas en San Luis Antioquia por año'},
    {'url': "https://www.datos.gov.co/resource/bz43-8ahq.csv?$query=SELECT%0A%20%20%60fecha_hecho%60%2C%0A%20%20%60cod_depto%60%2C%0A%20%20%60departamento%60%2C%0A%20%20%60cod_muni%60%2C%0A%20%20%60municipio%60%2C%0A%20%20%60zona%60%2C%0A%20%20%60sexo%60%2C%0A%20%20%60cantidad%60%0AWHERE%0A%20%20caseless_one_of(%60departamento%60%2C%20%22ANTIOQUIA%22)%0A%20%20AND%20caseless_one_of(%60municipio%60%2C%20%22SAN%20LUIS%22)%0AORDER%20BY%20%60fecha_hecho%60%20DESC%20NULL%20LAST", 'titulo': 'Delitos sexuales en San Luis Antioquia por año'},
    {'url': "https://www.datos.gov.co/resource/q2ib-t9am.csv?$query=SELECT%0A%20%20%60fecha_hecho%60%2C%0A%20%20%60cod_depto%60%2C%0A%20%20%60departamento%60%2C%0A%20%20%60cod_muni%60%2C%0A%20%20%60municipio%60%2C%0A%20%20%60cantidad%60%0AWHERE%0A%20%20caseless_one_of(%60departamento%60%2C%20%22ANTIOQUIA%22)%0A%20%20AND%20caseless_one_of(%60municipio%60%2C%20%22SAN%20LUIS%22)%0AORDER%20BY%20%60fecha_hecho%60%20DESC%20NULL%20LAST", 'titulo': 'Extorsión en San Luis Antioquia por año'}
]

# Crear lista de colores a partir de la paleta Spectral11
colores = Spectral11

st.set_page_config(page_title="Gráficos de Delitos en San Luis", layout="wide")

# Agregar fondo degradado
page_bg_img = '''
<style>
.stApp {
    background: linear-gradient(to bottom, #00c6ff, #0072ff);
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Mostrar el logo y el título
st.image("https://via.placeholder.com/150", width=150)  # Reemplaza con la URL del logo de la alcaldía de San Luis
st.title("ALCALDÍA DE SAN LUIS")

# Crear los gráficos y mostrarlos en Streamlit
for i, info in enumerate(info_graficos):
    grafico = crear_grafico(info['url'], info['titulo'], colores[i % len(colores)])
    if grafico:
        script, div = components(grafico)
        st.markdown(f"## {info['titulo']}")
        st.bokeh_chart(grafico)
