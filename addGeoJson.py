import folium

mapa = folium.Map(width=800, height=600, zoom_start=5.5,
                  location=[52, 19], tiles='Mapbox Bright')

powiaty_geojson = "geo_put.json"


folium.GeoJson(
    powiaty_geojson,
    name='geojson',
    style_function=lambda feature: {
        'color': 'black',
        'fillColor': '#fff',
        'weight': 1,
        'stroke': True,
        # 'dashArray': '5, 5'
    },
).add_to(mapa)
folium.LayerControl().add_to(mapa)


mapa.save("index.html")

