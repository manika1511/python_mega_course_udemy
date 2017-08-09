import folium
import pandas

data = pandas.read_csv("Volcanoes.csv")

latitude = list(data["LAT"])
longitude = list(data["LON"])
elevation = list(data["ELEV"])

def color_producer(elev):
    if elev < 1000:
        return "green"
    elif elev >=1000 and elev < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location = [40.42, -120.45])

fg = folium.FeatureGroup(name="My map")

for lat, lon, elev in zip(latitude, longitude, elevation):
    # fg.add_child(folium.Marker(location=[lat, lon], popup=str(elev)+"m", icon=folium.Icon(color=color_producer(elev))))
    fg.add_child(folium.CircleMarker(location=[lat, lon], popup=str(elev)+"m", radius=5, fill_color=color_producer(elev),
    color="grey", fill_opacity=0.7))

map.add_child(fg)

map.save("Map1.html", zoom=6, tiles="Mapbox Bright")
