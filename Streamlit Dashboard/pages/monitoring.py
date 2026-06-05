import streamlit as st
import plotly.express as px
from utils.data_loader import load_data
from utils.model_loader import load_model

df = load_data()
model = load_model()

def show_monitoring(df):
    
    st.title("📊 Monitoring")

    st.write(
        "CPU, Memory, Disk Monitoring"
    )

    fig = px.line(
    df,
    y="CPU_Usage_Percent",
    title="CPU Usage Trend")

    st.plotly_chart(
    fig,
    use_container_width=True)

    fig = px.line(
    df,
    y="Memory_Usage_MB",
    title="Memory Usage Trend")

    st.plotly_chart(
    fig,
    use_container_width=True)

    fig = px.line(
    df,
    y="Disk_Usage_Percent",
    title="Disk Usage Trend")

    st.plotly_chart(
    fig,
    use_container_width=True)
