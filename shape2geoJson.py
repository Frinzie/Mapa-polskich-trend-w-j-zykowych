import os
import shapefile
from json import dumps

# code from https://ocefpaf.github.io/python4oceanographers/blog/2015/02/02/cartopy_folium_shapefile/
# but has some changes

def shape2json(fname, outfile="geo_put.json"):
    reader = shapefile.Reader(fname)
    fields = reader.fields[1:]
    field_names = [field[0] for field in fields]

    data = []
    for sr in reader.shapeRecords():
        atr = dict(zip(field_names, sr.record))
        data.append(dict(type="Feature", geometry=geom, properties=atr))
            
    keys = ['CELLCODE', 'EOFORIGIN', 'NOFORIGIN']

    with open(outfile, "w") as geojson:
        geojson.write(dumps({"type": "FeatureCollection",
                             "features": data}, indent=2) + "\n")


fname = "POL_adm_shp/POL_adm2.shp"
shape2json(fname)
