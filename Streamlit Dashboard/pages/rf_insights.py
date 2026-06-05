import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_data
from utils.model_loader import load_model

df = load_data()
model = load_model()

def show_rf_insights(df):

    st.title(
        "🌳 Random Forest Insights"
    )

    st.write(
        "Feature Importance"
    )

    features = [ "CPU_Usage_Percent",
            "Memory_Usage_MB",
            "Disk_Usage_Percent",
            "Response_Time_ms",
            "Failed_Transactions",
            "Alert_Count",
            "Error_Count",
            "Retry_Count",
            "Escalation_Level"]
    X= df[features]
    importance_df = pd.DataFrame({

    "Feature": features,

    "Importance":
        model.feature_importances_})
    importance_df = (
    importance_df
    .sort_values(
        by="Importance",
        ascending=False))
    
    fig = px.bar(
    importance_df,
    x="Feature",
    y="Importance",
    title="Feature Importance")

    st.plotly_chart(
    fig,
    use_container_width=True)
    st.dataframe(
    importance_df)
    st.info(
    """
    Random Forest analyzes server metrics
    and predicts failure probability.
    Higher feature importance means the
    metric contributes more to predictions.
    """)
    


    