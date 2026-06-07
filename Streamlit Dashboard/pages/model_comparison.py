import streamlit as st
import pandas as pd

st.set_page_config(page_title="Model Comparison", layout="wide")

def show_model(df):

 st.title("📊 Model Comparison Dashboard")

# Load results
 results_df = pd.read_csv(r"C:\Users\kgeet\OneDrive\Desktop\PredictOps-AI\Streamlit Dashboard\pages\outputs\results.csv")


# Table
 st.subheader("📋 Model Performance Table")
 st.dataframe(results_df)

# Chart
 st.subheader("📊 Metrics Comparison")

 import plotly.express as px

 metrics_df = results_df.melt(
    id_vars="Model",
    value_vars=["Accuracy", "Precision", "Recall", "F1 Score", "ROC-AUC"],
    var_name="Metric",
    value_name="Score"
)

 fig = px.bar(
    metrics_df,
    x="Model",
    y="Score",
    color="Metric",
    barmode="group",
    title="Model Performance Comparison"
)

 fig.update_layout(
    xaxis_tickangle=-360
)

 st.plotly_chart(fig, use_container_width=True)