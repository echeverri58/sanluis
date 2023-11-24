import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Definir la URL
url = "https://www.datos.gov.co/resource/ntej-qq7v.csv?$query=SELECT%0A%20%20%60fecha_hecho%60%2C%0A%20%20%60cod_depto%60%2C%0A%20%20%60departamento%60%2C%0A%20%20%60cod_muni%60%2C%0A%20%20%60municipio%60%2C%0A%20%20%60cantidad%60%0AWHERE%0A%20%20caseless_one_of(%60departamento%60%2C%20%22ANTIOQUIA%22)%0A%20%20AND%20caseless_one_of(%60municipio%60%2C%20%22SAN%20LUIS%22)%0AORDER%20BY%20%60fecha_hecho%60%20DESC%20NULL%20LAST"

# Leer datos desde la URL
df = pd.read_csv(url)

# Configurar la aplicación Streamlit
st.title("Visualización de Datos")
st.subheader("Lesiones accidente tránsito en San Luis")

# Mostrar los primeros registros de los datos
st.write("Primeros registros de los datos:")
st.write(df.head())

# Gráfico de barras
fig, ax = plt.subplots()
ax.bar(df["fecha_hecho"], df["cantidad"])
plt.xlabel("Año")
plt.ylabel("Cantidad")
plt.title("Lesiones accidente tránsito San Luis")
st.pyplot(fig)

# Gráfico de dispersión
st.write("Gráfico de dispersión:")
st.scatter_chart(df[["fecha_hecho", "cantidad"]])

# Gráfico de línea
st.write("Gráfico de línea:")
st.line_chart(df[["fecha_hecho", "cantidad"]])

# Histograma
st.write("Histograma:")
st.hist(df["cantidad"], bins=10, edgecolor='black')

# Mapa de calor
st.write("Mapa de calor:")
st.heatmap(df.corr(), annot=True)

# Boxplot
st.write("Boxplot:")
st.box_plot(df["cantidad"])

# Resumen estadístico
st.write("Resumen estadístico:")
st.write(df.describe())

# Guardar el DataFrame en un archivo CSV (opcional)
# df.to_csv("datos_procesados.csv", index=False)

# Mostrar la aplicación
st.show()






