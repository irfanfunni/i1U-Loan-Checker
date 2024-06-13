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

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{

background: #030303;
background: linear-gradient(135deg, #030303, #302F2F);
}}
[data-testid="stSidebar"] > div:first-child {{
    background: #030303;
    background: linear-gradient(135deg, #030303, #302F2F);

</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.header("Bar Chart of The Frequency vs the States")
# Read the CSV file
df = pd.read_csv("./datasets/SBAnational.csv")

state_counts = df["State"].value_counts()

st.bar_chart(state_counts)
st.write()
st.divider()
st.write()
