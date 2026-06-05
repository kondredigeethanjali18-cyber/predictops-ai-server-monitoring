
import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    return pd.read_csv(
        "Dataset/Logging_Monitoring_Anomalies_Enhanced.csv"
    )



