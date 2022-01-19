#name: Britney Huiracocha
#email: britney.huiracocha44@myhunter.cuny.edu
#date: November 8,2020
#this program uses folium again to generate a map with markers for textile drop-off locations in NYC.

import pandas as pd
import folium

file1=input("Please enter the name of the input file: ")
file2=input("Please enter the name of the output file: ")
borough=input("Please enter the name of the borough: ")

dropoff=pd.read_csv(file1)
boroughMap=folium.Map(location=[40.75,-74.125])

dataCopy=data.groupby("Borough").get_group(borough)

for index,row in dataCopy.iterrows():
    lat=row["Latitude"]
    lon=row["Longitude"]
    address=row["Address"]
    marker=folium.Marker([lat,lon],popup=address)
    marker.add_to(boroughMap)

boroughMap.save(file2)
