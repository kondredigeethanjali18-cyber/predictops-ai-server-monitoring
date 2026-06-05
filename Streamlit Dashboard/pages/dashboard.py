import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_data
from utils.model_loader import load_model


def show_dashboard(df):

    st.title("🚀 PredictOps AI")
    st.subheader(
        "AI-Powered Server Monitoring & Failure Prediction"
    )

    # Load Data
    try:
        df = load_data()
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return

    # Load Model
    try:
        model = load_model()
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return

    st.markdown("---")

    # Total Records
    total_servers = len(df)

    # KPI Cards
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Records: ",total_servers)

    # CPU Average
    if "CPU_Usage_Percent" in df.columns:
        col2.metric(
            "Avg CPU %",
            round(df["CPU_Usage_Percent"].mean(), 2)
        )

    # Memory Average
    if "Memory_Usage_MB" in df.columns:
        col3.metric(
            "Avg Memory %",
            round(df["Memory_Usage_MB"].mean(), 2)
        )

    # Disk Average
    if "Disk_Usage_Percent" in df.columns:
        col4.metric(
            "Avg Disk %",
            round(df["Disk_Usage_Percent"].mean(), 2)
        )

    st.markdown("---")

    # Dataset Preview
    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    st.markdown("---")

    st.subheader(" Dataset Information")

    st.write(
        f"Rows: {df.shape[0]}"
    )

    st.write(
        f"Columns: {df.shape[1]}"
    )