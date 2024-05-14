import pandas as pd
import plotly.express as px
import streamlit as st
import json

PATH_TO_DATA = "./state_city_data.json"
PATH_TO_GEOJSON="indian_map_coordinates.geojson"

def state_city_scatter_mapbox():
    #Give a subtitle in the streamlit app
    st.subheader("Visualising state and capital cities of India - Scatter Map")
    #Loading state and city data from JSON file into a Pandas
    #Dataframe
    state_city_data = pd.read_json(PATH_TO_DATA)
    #Show a table
    st.dataframe(state_city_data, hide_index=True)
    #Plotly scatter plot
    fig = px.scatter_mapbox(data_frame=state_city_data,
                            lat="lat",
                            lon="long",
                            hover_data=["capital"],
                            color="capital",
                            zoom=3,
                            opacity=0.9,
                            height=600,
                            center={
                                "lat": 28.6,
                                "lon": 77.2
                            })
    #Basemap style
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"t": 0, "b": 0, "l": 0, "r":0})

    return st.plotly_chart(fig)

# The current data we have it is much more suitable to scatter map, because every specific location has specific longitude and latitude. The choropleth map is better for visualizing the data in a more geographical way or shading of data. e.g density of tree or forest in india or election results.

def state_city_choropleth_mapbox():
   #Give a subtitle in the streamlit app
   st.subheader("Visualising state and capital cities of India - Choropleth Map") 
   #Loading state and city data from JSON file into a Pandas
   #Dataframe
   state_city_data = pd.read_json(PATH_TO_DATA)
   #Show a table
   st.dataframe(state_city_data, hide_index=True)
   #Plotly choropleth plot
   fig = px.choropleth_mapbox(data_frame=state_city_data,
        hover_data=["capital"],
        locations="state",
        geojson=json.load(open(PATH_TO_GEOJSON, "r")),
        featureidkey="properties.ST_NM",
        color="capital",
        zoom=3,
        opacity=0.9,
        height=600,
        labels={"capital": "Capital City"},
        center={
            "lat": 28.6,
            "lon": 77.2
        })
    #Basemap style
    #options:open-street-map,carto-positron, carto-positron-nolabels
   fig.update_layout(mapbox_style="carto-darkmatter")
   fig.update_layout(margin={"t": 0, "b": 0, "l": 0, "r":0})
   return st.plotly_chart(fig)
     

    