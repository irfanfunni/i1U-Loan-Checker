#Import Modules
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Configure Page
st.set_page_config(
    page_title="Data Analysis",
    page_icon="💵",
)

st.header("Bar Chart of The Frequency vs the States")
# Read the CSV file
df = pd.read_csv("./datasets/SBAnational_cleaned.csv")

state_counts = df["State"].value_counts()

st.bar_chart(state_counts)
st.write()
st.divider()
st.write()
