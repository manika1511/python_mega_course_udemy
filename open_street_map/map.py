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

fgv = folium.FeatureGroup(name="Volcanoes")

for lat, lon, elev in zip(latitude, longitude, elevation):
    # fgv.add_child(folium.Marker(location=[lat, lon], popup=str(elev)+"m", icon=folium.Icon(color=color_producer(elev))))
    fgv.add_child(folium.CircleMarker(location=[lat, lon], popup=str(elev)+"m", radius=5, fill_color=color_producer(elev),
    color="grey", fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json','r', encoding="utf-8-sig"),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000<=x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html", zoom=6, tiles="Mapbox Bright")
