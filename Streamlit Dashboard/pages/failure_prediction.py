import streamlit as st
import plotly.express as px
import streamlit.components.v1 as components
from utils.model_loader import load_model


# ---------- RISK LEVEL FUNCTION ----------
def risk_level(prob):
    if prob >= 0.8:
        return "Critical"
    elif prob >= 0.5:
        return "Warning"
    else:
        return "Healthy"


def show_prediction(df):

    # ---------- HTML HEADER ----------
    st.markdown("""
    <div class="fp-header">
        <h1>🔮 Failure Prediction</h1>
        <p>AI-based server failure risk analysis using Random Forest</p>
    </div>

    <style>
    .fp-header {
        background: linear-gradient(90deg, #1e293b, #020617);
        padding: 22px;
        border-radius: 14px;
        margin-bottom: 25px;
    }
    .fp-header h1 {
        color: white;
        margin: 0;
    }
    .fp-header p {
        color: #cbd5e1;
        font-size: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------- LOAD MODEL ----------
    try:
        model = load_model()
    except Exception as e:
        st.error(f"Model loading failed: {e}")
        return

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

    # ---------- PREDICTIONS ----------
    df["Failure_Probability"] = model.predict_proba(X)[:, 1]
    df["Risk_Level"] = df["Failure_Probability"].apply(risk_level)

    avg_risk = round(df["Failure_Probability"].mean() * 100, 2)

    # ---------- HTML KPI CARD ----------
    st.markdown(f"""
    <div class="risk-card">
        <h3>Overall Failure Risk</h3>
        <p>{avg_risk}%</p>
    </div>

    <style>
    .risk-card {{
        background: #fee2e2;
        border-left: 6px solid #dc2626;
        padding: 18px;
        width: 280px;
        border-radius: 12px;
        margin-bottom: 25px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.12);
    }}
    .risk-card h3 {{
        margin: 0;
        color: #7f1d1d;
    }}
    .risk-card p {{
        font-size: 26px;
        font-weight: bold;
        margin-top: 8px;
    }}
    </style>
    """, unsafe_allow_html=True)

    # ---------- TOP RISK TABLE ----------
    st.subheader("🚨 Top High-Risk Records")

    top_risk = df.sort_values(
        "Failure_Probability", ascending=False
    ).head(10)

    st.dataframe(
        top_risk[
            ["Anomaly_ID", "Failure_Probability", "Risk_Level"]
        ],
        use_container_width=True
    )

    # ---------- BAR CHART ----------
    fig = px.bar(
        top_risk,
        x="Anomaly_ID",
        y="Failure_Probability",
        color="Risk_Level",
        title="Top Failure Risk Records"
    )

    st.plotly_chart(fig, use_container_width=True)

    # ---------- DISTRIBUTION ----------
    fig2 = px.histogram(
        df,
        x="Failure_Probability",
        nbins=20,
        title="Failure Probability Distribution"
    )

    st.plotly_chart(fig2, use_container_width=True)

    # ---------- RISK SUMMARY ----------
    st.subheader("📊 Risk Summary")
    st.write(df["Risk_Level"].value_counts())

    # ---------- JAVASCRIPT ----------
    components.html("""
    <script>
        console.log("Failure Prediction Page Loaded");
        alert("AI Failure Prediction Module Loaded Successfully!");
    </script>
    """, height=0)