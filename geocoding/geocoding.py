import pandas
from geopy.geocoders import Nominatim

df = pandas.read_csv("supermarkets.csv")

nom = Nominatim(scheme="http")

df["Address"] = df["Address"]+ ', ' + df["City"] + ', ' + df["State"] + ', ' + df['Country']
df["Coordinates"] = df["Address"].apply(nom.geocode)
df["Latitide"] = df["Coordinates"].apply(lambda x: x.latitude if x !=None else None)
df["Longitude"] = df["Coordinates"].apply(lambda x: x.longitude if x !=None else None)

print (df)