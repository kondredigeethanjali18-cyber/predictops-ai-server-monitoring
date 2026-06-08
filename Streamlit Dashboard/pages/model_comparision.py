import streamlit as st
import plotly.express as px
import streamlit.components.v1 as components
import pandas as pd


def show_model(df):

    # ---------- HTML HEADER ----------
    st.markdown("""
    <div class="mc-header">
        <h1>📈 Model Comparison</h1>
        <p>Performance comparison of machine learning models</p>
    </div>

    <style>
    .mc-header {
        background: linear-gradient(90deg, #312e81, #020617);
        padding: 22px;
        border-radius: 14px;
        margin-bottom: 25px;
    }
    .mc-header h1 {
        color: #ffffff;
        margin: 0;
    }
    .mc-header p {
        color: #c7d2fe;
        font-size: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------- MODEL METRICS (STATIC / EVALUATION RESULTS) ----------
    metrics_data = {
        "Model": ["Random Forest", "Logistic Regression", "XGBoost"],
        "Accuracy": [0.93, 0.86, 0.91],
        "Precision": [0.92, 0.84, 0.90],
        "Recall": [0.94, 0.85, 0.92],
        "F1 Score": [0.93, 0.84, 0.91]
    }

    metrics_df = pd.DataFrame(metrics_data)

    # ---------- HTML METRIC CARDS ----------
    st.markdown("""
    <div class="metric-note">
        <strong>Note:</strong> Metrics are obtained from offline model evaluation.
    </div>

    <style>
    .metric-note {
        background: #e0e7ff;
        padding: 12px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------- TABLE ----------
    st.subheader("📊 Evaluation Metrics")
    st.dataframe(metrics_df, use_container_width=True)

    # ---------- BAR CHART ----------
    fig = px.bar(
        metrics_df,
        x="Model",
        y=["Accuracy", "Precision", "Recall", "F1 Score"],
        barmode="group",
        title="Model Performance Comparison"
    )

    st.plotly_chart(fig, use_container_width=True)

    # ---------- BEST MODEL ----------
    best_model = metrics_df.sort_values(
        "Accuracy", ascending=False
    ).iloc[0]["Model"]

    st.markdown(f"""
    <div class="best-model">
        🏆 Best Performing Model: <strong>{best_model}</strong>
    </div>

    <style>
    .best-model {{
        background: #dcfce7;
        padding: 18px;
        border-radius: 14px;
        margin-top: 20px;
        font-size: 18px;
        font-weight: bold;
    }}
    </style>
    """, unsafe_allow_html=True)

    # ---------- JAVASCRIPT ----------
    components.html("""
    <script>
        console.log("Model Comparison Page Loaded");
        alert("Model Performance Comparison Ready!");
    </script>
    """, height=0)