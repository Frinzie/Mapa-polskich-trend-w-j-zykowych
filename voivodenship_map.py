import folium
from branca.colormap import linear
from voivodenship_dz_c import dict_dz_c


mapa = folium.Map(width=800, height=600, zoom_start=5.5,
                  location=[52, 19], tiles='Mapbox Bright')  # dzięki temu są 4 tile:
folium.TileLayer('stamentoner').add_to(mapa)                 # mapbox_bright wygląda obiecujaco oraz to ostatnie
folium.TileLayer('stamenwatercolor').add_to(mapa)            # stamenwatercolor wygląda cool, ale jest troszkę useless
folium.TileLayer('cartodbpositron').add_to(mapa)             # brak mi takich bez nazw państwa :(


voivodenship_json = "geo_voi.json"
colour_map = linear.RdPu.to_step(10)


folium.GeoJson(
    powiaty_geojson,
    name='geojson',
    style_function = lambda feature: {
        'fillColor': colour_map(dict_dz_c[feature['properties']['VARNAME_1']]), # koloruje „stany”
        'color': '#000',  # kolor granic
        'weight': 0,      # grubosć granic
        'stroke': True,   
        'fillOpacity': 1,  # !przezroczystość wypełnienia c'nie
    },
).add_to(mapa)
folium.LayerControl().add_to(mapa)


mapa.save("index.html")

