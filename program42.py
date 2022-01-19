#name: Britney Huiracocha
#email: britney.huiracocha44@myhunter.cuny.edu
#date: November 8,2020
#this program uses folium to make a map of NYC

import folium

mapCUNY=folium.Map(location=[40.75,-74.125],zoom_start=10)
folium.Marker(location=[40.768731,-73.964915],popup="Hunter College").add_to(mapCUNY)
mapCUNY.save(outfile='nycMap.html')
