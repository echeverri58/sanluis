import streamlit as st
import pandas as pd
from bokeh.plotting import figure
from bokeh.layouts import column, gridplot
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.palettes import Spectral11

# Configuración de la página
st.set_page_config(page_title="Delitos en San Luis, Antioquia", layout="wide")

# Estilos CSS personalizados
st.markdown("""
<style>
    .main {
        background: linear-gradient(to bottom, #1e3c72, #2a5298);
        color: white;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    h1 {
        color: white;
        text-align: center;
        padding: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# Título y logo
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("https://www.sanluisantioquia.gov.co/Uploads/Thumb/logo%20alcaldia%20de%20san%20luis.png", width=200)
st.title("Delitos en San Luis, Antioquia")

def crear_grafico(url, titulo, color):
    try:
        df = pd.read_csv(url)
        if df.empty:
            st.write(f"No hay datos para el gráfico: {titulo}")
            return None
        df['fecha_hecho'] = pd.to_datetime(df['fecha_hecho'], errors='coerce')
        df = df.dropna(subset=['fecha_hecho'])
        df['año'] = df['fecha_hecho'].dt.year
        cantidad_por_año = df.groupby('año')['cantidad'].sum().astype(int)
        años = sorted(cantidad_por_año.index.astype(str))

        if len(años) == 0:
            st.write(f"No hay datos válidos para el gráfico: {titulo}")
            return None

        source = ColumnDataSource(data=dict(
            year=años,
            cantidad=cantidad_por_año.values
        ))

        p = figure(title=titulo, x_range=años, height=300, width=300, toolbar_location=None, tools="")

        p.vbar(x='year', top='cantidad', width=0.9, source=source, line_color='white', fill_color=color)

        p.xgrid.grid_line_color = None
        p.y_range.start = 0
        p.xaxis.axis_label = 'Año'
        p.yaxis.axis_label = 'Cantidad'
        p.axis.minor_tick_line_color = None
        p.outline_line_color = None
        p.title.text_color = "white"
        p.xaxis.major_label_text_color = "white"
        p.yaxis.major_label_text_color = "white"
        p.xaxis.axis_label_text_color = "white"
        p.yaxis.axis_label_text_color = "white"

        p.xaxis.major_label_orientation = -3.14 / 2  # -90 grados

        hover = HoverTool(tooltips=[('Año', '@year'), ('Cantidad', '@cantidad')])
        p.add_tools(hover)

        return p
    except Exception as e:
        st.write(f"Error al crear el gráfico {titulo}: {str(e)}")
        return None

# Ejemplo de URLs y títulos (mismo que en el código original)
info_graficos = [
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

    # Añadir más gráficos según sea necesario
]

# Crear lista de colores a partir de la paleta Spectral11
colores = Spectral11

# Crear los gráficos y mostrarlos en Streamlit
graficos = []
for i, info in enumerate(info_graficos):
    grafico = crear_grafico(info['url'], info['titulo'], colores[i % len(colores)])
    if grafico:
        graficos.append(grafico)

# Mostrar los gráficos en una cuadrícula
if graficos:
    grid = gridplot([graficos[i:i+3] for i in range(0, len(graficos), 3)])
    st.bokeh_chart(grid, use_container_width=True)
else:
    st.write("No se crearon gráficos debido a la falta de datos válidos.")

# Agregar información adicional
st.markdown("""
## Acerca de este dashboard

Este dashboard muestra estadísticas de diferentes tipos de delitos en el municipio de San Luis, Antioquia. 
Los datos son obtenidos de fuentes oficiales y se actualizan periódicamente.

Para más información, visite el [sitio web oficial de San Luis, Antioquia](https://www.sanluisantioquia.gov.co/).
""")

# Agregar footer
st.markdown("""
---
Desarrollado por [Tu Nombre/Organización] | Datos proporcionados por [Fuente de Datos]
""")

