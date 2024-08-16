import streamlit as st
import folium
from streamlit_folium import st_folium
import geopandas as gpd

def main():
    st.title("Meu WebGIS com Streamlit e Folium")

    # Preparar espaço para o mapa
    map_placeholder = st.empty()

    # Carregar dados
    data = gpd.GeoDataFrame({
        'city': ["New York", "Los Angeles", "Chicago", "Miami"],
        'latitude': [40.7128, 34.0522, 41.8781, 25.7617],
        'longitude': [-74.0060, -118.2437, -87.6298, -80.1918]
    }, geometry=gpd.points_from_xy(data['longitude'], data['latitude']))

    city_to_filter = st.selectbox('Escolha uma cidade para mostrar no mapa:', data['city'].unique())
    filtered_data = data[data['city'] == city_to_filter]

    if not filtered_data.empty:
        first_point = filtered_data.iloc[0]
        m = folium.Map(location=[first_point['latitude'], first_point['longitude']], zoom_start=10)
        folium.Marker(
            location=[first_point['latitude'], first_point['longitude']],
            popup=first_point['city']
        ).add_to(m)
        # Atualizar o espaço reservado com o novo mapa
        map_placeholder.folium(m, width=725, height=500)
    else:
        map_placeholder.text("Nenhuma cidade selecionada ou dados disponíveis.")

if __name__ == "__main__":
    main()
