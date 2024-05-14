import streamlit as st
from state_city_map import state_city_scatter_mapbox, state_city_choropleth_mapbox
from aa_flight_paths import aa_flight_paths
from global_companies_map import global_companies_map

st.set_page_config(layout="wide")
st.title("State Capital Finder")

SIDEBAR_DICT = {
    "Global COMPANIES MAP": global_companies_map,
    "AA FLIGHT PATHS": aa_flight_paths,
    "STATE-CITY SCATTER MAP": state_city_scatter_mapbox,
    "STATE-CITY CHOROPLETH MAP": state_city_choropleth_mapbox
}


def main():
  chart_type = st.sidebar.radio("Select chart type:", SIDEBAR_DICT.keys())
  if chart_type is not None:
      SIDEBAR_DICT[chart_type]()


if __name__ == "__main__":
  main()
