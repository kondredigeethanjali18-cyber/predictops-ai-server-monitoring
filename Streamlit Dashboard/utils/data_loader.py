import pandas as pd
import streamlit as st
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR.parent / "Dataset" / "Logging_Monitoring_Anomalies_Enhanced.csv"

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)