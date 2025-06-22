import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Datos
invitados = [
    {"name": "Jan", "location": "Rotterdam", "guest_of": "Hardwell", "favourite_dj": "Tiesto"},
    {"name": "Piet", "location": "Amsterdam", "guest_of": "Tiesto", "favourite_dj": "DaftPunk"},
    {"name": "John", "location": "Cartagena", "guest_of": "Tiesto", "favourite_dj": "Avici"},
    {"name": "Daniela", "location": "Bogota", "guest_of": "Afrojack", "favourite_dj": "Tiesto"},
    {"name": "Almeja", "location": "Munchen", "guest_of": "Afrojack", "favourite_dj": "Matrin Garrix"},
    {"name": "Valentina", "location": "New York", "guest_of": "Hardwell", "favourite_dj": "Armin van Buuren"},
    {"name": "Chris", "location": "Miami", "guest_of": "Afrojack", "favourite_dj": "Don Diablo"},
    {"name": "Mack", "location": "Los Angeles", "guest_of": "Hardwell", "favourite_dj": "Oliver Heldens"},
    {"name": "Henry", "location": "Singapore", "guest_of": "Tiesto", "favourite_dj": "Matrin Garrix"},
    {"name": "Ineke", "location": "Berlin", "guest_of": "Afrojack", "favourite_dj": "Avici"},
]

# DataFrame
df = pd.DataFrame(invitados)

# Streamlit App
st.title("🎧 DJ Guest Dashboard")

# Filtros
st.sidebar.header("Filtros")
all_djs = df['guest_of'].unique().tolist()
all_locations = df['location'].unique().tolist()

selected_djs = st.sidebar.multiselect("Selecciona DJ(s) anfitriones:", all_djs, default=all_djs)
selected_locations = st.sidebar.multiselect("Selecciona ubicaciones:", all_locations, default=all_locations)

# Filtrar datos
df_filtrado = df[df['guest_of'].isin(selected_djs) & df['location'].isin(selected_locations)]

# Sección 1: Invitados por DJ
st.header("Invitados por DJ")
invitados_por_dj = df_filtrado['guest_of'].value_counts()
st.bar_chart(invitados_por_dj)

# Sección 2: DJ favorito del mundo
st.header("DJ Favorito del Mundo")
dj_favorito = df_filtrado['favourite_dj'].value_counts()
st.bar_chart(dj_favorito)

# Sección 3: Personas por ubicación
st.header("Personas por Ubicación")
personas_ubicacion = df_filtrado['location'].value_counts()
st.bar_chart(personas_ubicacion)

# Tabla general
st.header("Tabla de Datos de Invitados")
st.dataframe(df_filtrado)

# Extra: Mapa de ubicaciones
st.header("🗺️ Mapa de ubicaciones de invitados")
coordenadas = {
    "Rotterdam": (51.9225, 4.4792),
    "Amsterdam": (52.3676, 4.9041),
    "Cartagena": (10.3910, -75.4794),
    "Bogota": (4.7110, -74.0721),
    "Munchen": (48.1351, 11.5820),
    "New York": (40.7128, -74.0060),
    "Miami": (25.7617, -80.1918),
    "Los Angeles": (34.0522, -118.2437),
    "Singapore": (1.3521, 103.8198),
    "Berlin": (52.5200, 13.4050)
}
df_filtrado['lat'] = df_filtrado['location'].map(lambda loc: coordenadas[loc][0])
df_filtrado['lon'] = df_filtrado['location'].map(lambda loc: coordenadas[loc][1])
st.map(df_filtrado[['lat', 'lon']])

# Extra: Descargar CSV
st.header("📥 Exportar Datos")
csv = df_filtrado.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Descargar datos filtrados como CSV",
    data=csv,
    file_name='invitados_filtrados.csv',
    mime='text/csv',
)
