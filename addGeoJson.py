import folium
import numpy as np



mapa = folium.Map(width=650, height=500, zoom_start=5,
                  location=[52, 19]).                  # Bolzga's location

powiaty_geojson = "geo_put.json".  # the geojson file

folium.GeoJson(
    powiaty_geojson,
    name='geojson',
    style_function=lambda feature: {    # I don't know why this doesn't work and show the counties' borders on map
        'color': 'black',
        'weight': 4,
        'stroke': True,
        # 'dashArray': '5, 5'
    },

).add_to(mapa)
folium.LayerControl().add_to(mapa)

# mapa.save("index.html")
