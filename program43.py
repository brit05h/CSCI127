#name: Britney Huiracocha
#email: britney.huiracocha44@myhunter.cuny.edu
#date: November 8,2020
#this program asks the user for the name of a CSV file

import folium
import pandas as pd

file=input("Enter CSV file name: ")
thfile=input("Enter name of output file: ")

collisions=pd.read_csv(file)
m=folium.Map(location=40.76731,-73.964915])
tiles="Cartodb Positron"

for index,row in collisions.iterrows():
    lat=row["LATITUDE"]
    lon=row["LONGITUDE"]
    name=row["TIME"]
    newMarker=folium.Marker([lat,lon],popup=name).add_to(m)
    newMarker.add_to(m)
m.save(thfile=output)
