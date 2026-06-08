import streamlit as st
import streamlit.components.v1 as components
from utils.model_loader import load_model


def risk_level(prob):
    if prob >= 0.8:
        return "Critical"
    elif prob >= 0.5:
        return "Warning"
    else:
        return "Healthy"


def get_recommendation(risk):
    if risk == "Critical":
        return "Immediate action required! Scale resources, check logs, notify DevOps team."
    elif risk == "Warning":
        return "Monitor closely and optimize workloads."
    else:
        return "System healthy. No immediate action required."


def show_recommendations(df):

    # ---------- HEADER ----------
    st.markdown("""
    <div class="rec-header">
        <h1>🧠 AI Recommendations</h1>
        <p>Automated actions based on server health and failure risk</p>
    </div>
    """, unsafe_allow_html=True)

    # ---------- LOAD MODEL ----------
    model = load_model()

    features = [
        "CPU_Usage_Percent",
        "Memory_Usage_MB",
        "Disk_Usage_Percent",
        "Response_Time_ms",
        "Failed_Transactions",
        "Retry_Count",
        "Alert_Count",
        "Error_Count",
        "Escalation_Level"
    ]

    X = df[features]

    # 🔥 ALWAYS COMPUTE HERE
    df["Failure_Probability"] = model.predict_proba(X)[:, 1]
    df["Risk_Level"] = df["Failure_Probability"].apply(risk_level)
    df["Recommendation"] = df["Risk_Level"].apply(get_recommendation)

    # ---------- COUNTS ----------
    st.subheader("📊 Risk Summary")
    st.write(df["Risk_Level"].value_counts())

    # ---------- SERVER ACTION TABLE ----------
    st.subheader("🚨 Servers Requiring Action")
    st.dataframe(
        df[
            ["Anomaly_ID", "Risk_Level", "Recommendation"]
        ].sort_values("Risk_Level"),
        use_container_width=True
    )

    # ---------- JS ----------
    components.html("""
    <script>
        console.log("Recommendations ready");
    </script>
    """, height=0)