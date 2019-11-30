import argparse

import pandas as pd
import folium
from folium.plugins import MarkerCluster

parser = argparse.ArgumentParser(description="""Crea un mapa html (usando folium/leaflet) usando el csv de entrada. El csv debe tener las columnas: lat, log y title""")
parser.add_argument('--lat', required=True,  help='latitud inicial')
parser.add_argument('--log', required=True, help='longitud inicial')
parser.add_argument('--zoom', required=True, help='nivel de zoom inicial')
parser.add_argument('--input', required=True, help='path al csv de entrada')
parser.add_argument('--out', required=True, help='path/nombre de la salida')

args = parser.parse_args()

zoom_start = args.zoom
lat_init = args.lat
log_init = args.log
path_input = args.input
path_out = args.out

df = pd.read_csv(path_input)

m = folium.Map(location=[lat_init, log_init], zoom_start=zoom_start)
feature_group = folium.FeatureGroup(name='group')
marker_cluster = MarkerCluster()

for row in df.itertuples():
    marker = folium.Marker([row.latitud, row.longitud], popup=row.lugar)
    marker_cluster.add_child(marker)

feature_group.add_child(marker_cluster)
m.add_child(feature_group)

m.save(path_out)
