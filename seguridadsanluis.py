import streamlit as st
import pandas as pd
import plotly.express as px

# Definir la URL
url = "https://www.datos.gov.co/resource/ntej-qq7v.csv?$query=SELECT%0A%20%20%60fecha_hecho%60%2C%0A%20%20%60cod_depto%60%2C%0A%20%20%60departamento%60%2C%0A%20%20%60cod_muni%60%2C%0A%20%20%60municipio%60%2C%0A%20%20%60cantidad%60%0AWHERE%0A%20%20caseless_one_of(%60departamento%60%2C%20%22ANTIOQUIA%22)%0A%20%20AND%20caseless_one_of(%60municipio%60%2C%20%22SAN%20LUIS%22)%0AORDER%20BY%20%60fecha_hecho%60%20DESC%20NULL%20LAST"

# Leer datos desde la URL
df = pd.read_csv(url)

# Configurar la aplicación Streamlit
st.title("Visualización de Datos")
st.subheader("Lesiones accidente tránsito en San Luis")

# Gráfico de dispersión con Plotly
st.write("Gráfico de dispersión:")
fig = px.scatter(df, x="fecha_hecho", y="cantidad", title="Lesiones accidente tránsito San Luis")
st.plotly_chart(fig)

# Otros gráficos interactivos con Plotly
# Puedes explorar otros tipos de gráficos interactivos de Plotly según tus necesidades.

# Guardar el DataFrame en un archivo CSV (opcional)
# df.to_csv("datos_procesados.csv", index=False)

# Mostrar la aplicación
st.show()

