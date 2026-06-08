import streamlit as st
import plotly.express as px
import streamlit.components.v1 as components
import pandas as pd
from utils.model_loader import load_model


def show_rf_insights(df):

    # ---------- HTML HEADER ----------
    st.markdown("""
    <div class="rf-header">
        <h1>🌲 Random Forest Insights</h1>
        <p>Feature importance analysis for server failure prediction</p>
    </div>

    <style>
    .rf-header {
        background: linear-gradient(90deg, #065f46, #022c22);
        padding: 22px;
        border-radius: 14px;
        margin-bottom: 25px;
    }
    .rf-header h1 {
        color: #ecfdf5;
        margin: 0;
    }
    .rf-header p {
        color: #a7f3d0;
        font-size: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------- LOAD MODEL ----------
    try:
        model = load_model()
    except Exception as e:
        st.error(f"Failed to load model: {e}")
        return

    # ---------- CHECK FEATURE IMPORTANCE ----------
    if not hasattr(model, "feature_importances_"):
        st.warning("Feature importance not available for this model.")
        return

    # ---------- BUILD FEATURE IMPORTANCE DATAFRAME ----------
    importance_df = pd.DataFrame({
        "Feature": model.feature_names_in_,
        "Importance": model.feature_importances_
    }).sort_values("Importance", ascending=False)

    # ---------- SUMMARY CARD ----------
    top_feature = importance_df.iloc[0]["Feature"]

    st.markdown(f"""
    <div class="top-feature">
        🔍 Most Influential Feature:
        <strong>{top_feature}</strong>
    </div>

    <style>
    .top-feature {{
        background: #ecfeff;
        padding: 16px;
        border-radius: 12px;
        margin-bottom: 20px;
        font-size: 18px;
        font-weight: bold;
    }}
    </style>
    """, unsafe_allow_html=True)

    # ---------- BAR CHART ----------
    fig = px.bar(
        importance_df,
        x="Importance",
        y="Feature",
        orientation="h",
        title="Feature Importance (Random Forest)",
        color="Importance",
        color_continuous_scale="greens"
    )

    st.plotly_chart(fig, use_container_width=True)

    # ---------- TABLE ----------
    st.subheader("📊 Feature Importance Table")
    st.dataframe(importance_df, use_container_width=True)

    # ---------- INTERPRETATION ----------
    st.subheader("🧠 Interpretation")
    st.markdown("""
    - Features with higher importance contribute more to predicting server failure.
    - This helps DevOps teams focus on the most critical system metrics.
    - Random Forest provides built-in explainability compared to black-box models.
    """)

    # ---------- JAVASCRIPT ----------
    components.html("""
    <script>
        console.log("Random Forest Insights Loaded");
        alert("Random Forest Feature Importance Analysis Ready!");
    </script>
    """, height=0)