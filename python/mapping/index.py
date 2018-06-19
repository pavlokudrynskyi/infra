import folium
import pandas
import time

#Parse file with data
data=pandas.read_csv("data/university.csv")
name=list(data["University"])
rate=list(data["Rate"])
lat=list(data["Lat"])
lon=list(data["Lon"])


def color_mark(rate):
    if rate<0:
        raise ValueError("Rate cannot be < 0")
    if rate>8.0:
        return "green", "check"
    elif 5.0 <= rate <= 8.0:
        return "orange", "cloud"
    else:
        return "red", "info-sign"

#Start point on map
def main():
    nau_position=[50.439895, 30.430243]
    map=folium.Map(location=nau_position, zoom_start=5)
    fg_name=folium.FeatureGroup(name="University Name")

    #Show Markers on map
    for lt, ln, nm, rt in zip(lat, lon, name, rate):
        color_temp, icon_temp=color_mark(rt)
        fg_name.add_child(folium.Marker(location=[lt, ln], popup=str(nm + "\n" + str(rt)), icon=folium.Icon(color=color_temp, icon=icon_temp)))

    fg_poligon=folium.FeatureGroup(name="Poligon")
    fg_poligon.add_child(folium.GeoJson(data=open('data/countries.geo.json', 'r', encoding='utf-8-sig').read()))

    fg_layer_one=folium.FeatureGroup(name="MapBox Bright")
    fg_layer_one.add_child(folium.TileLayer('MapBox Bright'))

    fg_layer_two=folium.FeatureGroup(name="Mapbox Control Room")
    fg_layer_one.add_child(folium.TileLayer('Mapbox Control Room'))

    map.add_child(fg_name)
    map.add_child(fg_poligon)
    map.add_child(fg_layer_one)
    map.add_child(folium.LayerControl())

    map.save("index.html")
def sleep():
    time.sleep(500)
if __name__ == '__main__':
    main()
    sleep()
