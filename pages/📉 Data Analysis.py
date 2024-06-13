import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut


st.set_page_config(
    page_title="Data Analysis",
    page_icon="🌈",
)

st.header("Bar Chart of The Frequency vs the States")
# Read the CSV file
df = pd.read_csv("./datasets/SBAnational.csv")

state_counts = df["State"].value_counts()

st.bar_chart(state_counts)
st.write()
st.divider()
st.write()

# st.header("Graph of...")

# # Predefined dictionary of state abbreviations to their latitudes and longitudes
# state_coords = {
#     'IN': (40.2672, -86.1349),
#     'OK': (35.0078, -97.0929),
#     'FL': (27.9944, -81.7603),
#     'CT': (41.6032, -73.0877),
#     'NJ': (40.0583, -74.4057),
#     'NC': (35.7596, -79.0193),
#     'IL': (40.6331, -89.3985),
#     'RI': (41.5801, -71.4774),
#     'TX': (31.9686, -99.9018),
#     'VA': (37.4316, -78.6569),
#     'TN': (35.5175, -86.5804),
#     'AR': (35.2010, -91.8318),
#     'MN': (46.7296, -94.6859),
#     'MO': (37.9643, -91.8318),
#     'MA': (42.4072, -71.3824),
#     'CA': (36.7783, -119.4179),
#     'SC': (33.8361, -81.1637),
#     'LA': (30.9843, -91.9623),
#     'IA': (41.8780, -93.0977),
#     'OH': (40.4173, -82.9071),
#     'KY': (37.8393, -84.2700),
#     'MS': (32.3547, -89.3985),
#     'NY': (43.2994, -74.2179),
#     'MD': (39.0458, -76.6413),
#     'PA': (41.2033, -77.1945),
#     'OR': (43.8041, -120.5542),
#     'ME': (45.2538, -69.4455),
#     'KS': (39.0119, -98.4842),
#     'MI': (44.3148, -85.6024),
#     'AK': (61.3707, -152.4044),
#     'WA': (47.7511, -120.7401),
#     'CO': (39.5501, -105.7821),
#     'MT': (46.8797, -110.3626),
#     'WY': (43.0759, -107.2903),
#     'UT': (39.3200, -111.0937),
#     'NH': (43.1939, -71.5724),
#     'WV': (38.5976, -80.4549),
#     'ID': (44.0682, -114.7420),
#     'AZ': (34.0489, -111.0937),
#     'NV': (38.8026, -116.4194),
#     'WI': (43.7844, -88.7879),
#     'NM': (34.5199, -105.8701),
#     'GA': (32.1656, -82.9001),
#     'ND': (47.5515, -101.0020),
#     'VT': (44.5588, -72.5778),
#     'AL': (32.3182, -86.9023),
#     'NE': (41.4925, -99.9018),
#     'SD': (43.9695, -99.9018),
#     'HI': (19.8968, -155.5828),
#     'DE': (38.9108, -75.5277),
#     'DC': (38.9072, -77.0369)
# }

# # Example list of state abbreviations
# states = ['IN', 'OK', 'FL', 'CT', 'NJ', 'NC', 'IL', 'RI', 'TX', 'VA', 'TN', 'AR', 'MN', 'MO',
#           'MA', 'CA', 'SC', 'LA', 'IA', 'OH', 'KY', 'MS', 'NY', 'MD', 'PA', 'OR', 'ME', 'KS',
#           'MI', 'AK', 'WA', 'CO', 'MT', 'WY', 'UT', 'NH', 'WV', 'ID', 'AZ', 'NV', 'WI', 'NM',
#           'GA', 'ND', 'VT', 'AL', 'NE', 'SD', 'HI', 'DE', 'DC']

# # Create a DataFrame to store states and their coordinates
# state_data = {
#     'lat': [state_coords[state][0] for state in states],
#     'lon': [state_coords[state][1] for state in states]
# }

# df1 = pd.DataFrame(state_data)

# map_content = pd.DataFrame(state_counts,columns=['lat', 'lon'])
# st.map(df1)

# # zipcodes = df["Zip"].drop_duplicates()
# # # Initialize the geocoder
# # geolocator = Nominatim(user_agent="zipcode_to_latlong")

# # # Function to get latitude and longitude from a ZIP code
# # def get_lat_long(zipcode):
# #     try:
# #         location = geolocator.geocode({"postalcode": zipcode, "countryRegion": "US"})
# #         if location:
# #             return (location.latitude, location.longitude)
# #         else:
# #             return (None, None)
# #     except GeocoderTimedOut:
# #         return get_lat_long(zipcode)


# # # Collated Coordinates
# # total_coordinates = pd.DataFrame([get_lat_long(zipcode) for zipcode in zipcodes])

# # st.map(total_coordinates)