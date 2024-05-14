from geopy.geocoders import Nominatim, Photon
import folium as fo
import pandas as pd
from streamlit import components
import streamlit as st
import streamlit.components.v1 as components
from folium.plugins import MarkerCluster
from geopy.exc import GeocoderTimedOut, GeocoderQuotaExceeded

PATH_TO_DATA="companies_data.csv"

def global_companies_map():
  #Add a subtitle
  st.subheader("Global Distribution of Top Companies")
  #load companies into pandas dataframe, define index column
  companies_data=pd.read_csv(PATH_TO_DATA, index_col="Ranking")
  st.dataframe(companies_data)

  #slice and show a range of rows
  companies_data=companies_data[0:50]
  
  #Show a table
  st.dataframe(companies_data[["Company","Country"]])
  
  #initialise a geocoder with an user agent
  geolocator = Nominatim(user_agent="bashlik_user_agent")
  #create a folium map
  map = fo.Map(location=(20,0),
   zoom_start=2,
   tiles="cartodb positron")
  #add a marker cluster to handle multiple markers
  marker_cluster = MarkerCluster().add_to(map)

  #iterate over the dataframe rows
  for index, row in companies_data.iterrows():
    country_query = row['Country']
    try:
      location=geolocator.geocode(country_query, language='en')
      if location:
        st.write(f"Geocoding result for {row['Company']}, {country_query}: {location.address}")
        # st.write(f"{country_query }:[{location.latitude, location.longitude}]")
        popup_message=f"{row['Company']}, {row['Country']}"
        fo.Marker(location=[location.latitude, location.longitude],
        popup=popup_message).add_to(marker_cluster)
      else:
        st.error(f"Geocoding failed for {index}: {country_query}")
    except (GeocoderTimedOut, GeocoderQuotaExceeded,Exception) as e:
     st.error(f"Geocoding error:{e} for {country_query}")
  
  #save the map as HTML file
  map.save("companies_map.html")
  HtmlFile=open("companies_map.html","r",encoding="utf-8")
  my_map=HtmlFile.read()
  components.html(my_map,height=700)
  
  
   