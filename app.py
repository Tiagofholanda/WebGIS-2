import subprocess
import pkg_resources
import streamlit as st
import folium
from streamlit_folium import st_folium
import geopandas as gpd

required_packages = {
    'streamlit': '1.12.0',
    'folium': '0.12.1',
    'geopandas': '0.11.1',
    'streamlit-folium': '0.2.0'
}

installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}

# Instala pacotes faltantes ou desatualizados
for package, version in required_packages.items():
    if package not in installed_packages or installed_packages[package] != version:
        subprocess.check_call([sys.executable, "-m", "pip", "install", f"{package}=={version}"])

def main():
    st.title("Meu WebGIS com Streamlit e Folium")

    # Carregar ou criar dados geoespaciais
    data = gpd.GeoDataFrame({
        'city': ["New York", "Los Angeles", "Chicago"],
        'latitude': [40.7128, 34.0522, 41.8781],
        'longitude': [-74.0060, -118.2437, -87.6298]
    }, geometry=gpd.points_from_xy(data['longitude'], data['latitude']))

    # Criar um mapa com a localização centralizada
    m = folium.Map(location=[39.8283, -98.5795], zoom_start=4)

    # Adicionar pontos ao mapa
    for _, row in data.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=row['city']
        ).add_to(m)

    # Renderizar o mapa no Streamlit
    st_folium(m, width=725, height=500)

if __name__ == "__main__":
    main()
