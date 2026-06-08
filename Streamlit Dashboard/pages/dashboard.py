import streamlit as st
import plotly.express as px
import streamlit.components.v1 as components

def show_dashboard(df):

    # ---------- HTML + CSS HEADER ----------
    st.markdown("""
    <div class="html-header">
        <h1>PredictOps AI</h1>
        <p>AI-Powered Server Monitoring & Failure Prediction</p>
    </div>

    <style>
    .html-header {
        background: linear-gradient(90deg, #020617, #0f172a);
        padding: 25px;
        border-radius: 14px;
        margin-bottom: 25px;
    }
    .html-header h1 {
        color: #ffffff;
        margin: 0;
    }
    .html-header p {
        color: #cbd5e1;
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ---------- KPI CALCULATIONS ----------
    total_records = len(df)
    avg_cpu = round(df["CPU_Usage_Percent"].mean(), 2)
    avg_mem = round(df["Memory_Usage_MB"].mean(), 2)
    avg_disk = round(df["Disk_Usage_Percent"].mean(), 2)

    # ---------- HTML KPI CARDS ----------
    st.markdown(f"""
    <div class="card-container">
        <div class="card">
            <h3>Total Records</h3>
            <p>{total_records}</p>
        </div>
        <div class="card">
            <h3>Avg CPU (%)</h3>
            <p>{avg_cpu}</p>
        </div>
        <div class="card">
            <h3>Avg Memory (MB)</h3>
            <p>{avg_mem}</p>
        </div>
        <div class="card">
            <h3>Avg Disk (%)</h3>
            <p>{avg_disk}</p>
        </div>
    </div>

    <style>
    .card-container {{
        display: flex;
        gap: 20px;
        margin-bottom: 30px;
    }}
    .card {{
        background: #f8fafc;
        padding: 20px;
        border-radius: 12px;
        width: 220px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.12);
    }}
    .card h3 {{
        margin-bottom: 10px;
    }}
    .card p {{
        font-size: 22px;
        font-weight: bold;
    }}
    </style>
    """, unsafe_allow_html=True)

    # ---------- HEALTH OVERVIEW ----------
    if "Predicted_Failure" in df.columns:
        st.subheader("🩺 System Health Overview")

        df["Health_Status"] = df["Predicted_Failure"].map(
            {0: "Healthy", 1: "Unhealthy"}
        )

        fig = px.pie(
            df,
            names="Health_Status",
            title="Healthy vs Unhealthy Records",
            hole=0.4
        )

        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # ---------- DATA PREVIEW ----------
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.markdown("---")

    # ---------- DATASET INFO ----------
    st.subheader("Dataset Information")
    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")

    # ---------- JAVASCRIPT ----------
    components.html("""
    <script>
    console.log("PredictOps AI Dashboard Loaded");
    alert("Welcome to PredictOps AI Dashboard!");
    </script>
    """, height=0)