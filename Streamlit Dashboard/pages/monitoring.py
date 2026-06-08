import streamlit as st
import plotly.express as px
import streamlit.components.v1 as components


def show_monitoring(df):

    # ---------- HTML HEADER ----------
    st.markdown("""
    <div class="monitor-header">
        <h1>📡 Live Server Monitoring</h1>
        <p>Real-time system metrics and anomaly detection overview</p>
    </div>

    <style>
    .monitor-header {
        background: linear-gradient(90deg, #064e3b, #022c22);
        padding: 22px;
        border-radius: 14px;
        margin-bottom: 25px;
    }
    .monitor-header h1 {
        color: #ecfdf5;
        margin: 0;
    }
    .monitor-header p {
        color: #a7f3d0;
        font-size: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------- HEALTH STATUS ----------
    if "Predicted_Failure" in df.columns:
        df["Health_Status"] = df["Predicted_Failure"].map(
            {0: "Healthy", 1: "Unhealthy"}
        )
    else:
        st.warning("Prediction data not available")
        return

    # ---------- SUMMARY COUNTS ----------
    healthy_count = (df["Health_Status"] == "Healthy").sum()
    unhealthy_count = (df["Health_Status"] == "Unhealthy").sum()

    # ---------- HTML STATUS CARDS ----------
    st.markdown(f"""
    <div class="status-container">
        <div class="status-card healthy">
            <h3>Healthy Servers</h3>
            <p>{healthy_count}</p>
        </div>
        <div class="status-card unhealthy">
            <h3>Unhealthy Servers</h3>
            <p>{unhealthy_count}</p>
        </div>
    </div>

    <style>
    .status-container {{
        display: flex;
        gap: 25px;
        margin-bottom: 30px;
    }}
    .status-card {{
        padding: 22px;
        width: 260px;
        border-radius: 14px;
        color: white;
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }}
    .healthy {{
        background: linear-gradient(135deg, #16a34a, #14532d);
    }}
    .unhealthy {{
        background: linear-gradient(135deg, #dc2626, #7f1d1d);
    }}
    .status-card p {{
        font-size: 28px;
        font-weight: bold;
        margin-top: 10px;
    }}
    </style>
    """, unsafe_allow_html=True)

    # ---------- CPU & MEMORY MONITOR ----------
    st.subheader("📊 Resource Utilization")

    col1, col2 = st.columns(2)

    with col1:
        fig_cpu = px.histogram(
            df,
            x="CPU_Usage_Percent",
            nbins=20,
            title="CPU Usage Distribution (%)"
        )
        st.plotly_chart(fig_cpu, use_container_width=True)

    with col2:
        fig_mem = px.histogram(
            df,
            x="Memory_Usage_MB",
            nbins=20,
            title="Memory Usage Distribution (MB)"
        )
        st.plotly_chart(fig_mem, use_container_width=True)

    # ---------- HEALTH PIE ----------
    st.subheader("🩺 System Health Overview")

    fig_pie = px.pie(
        df,
        names="Health_Status",
        title="Healthy vs Unhealthy Servers",
        hole=0.4
    )

    st.plotly_chart(fig_pie, use_container_width=True)

    # ---------- DATA TABLE ----------
    st.subheader("📋 Monitoring Records")
    st.dataframe(
        df[
            [
                "Anomaly_ID",
                "CPU_Usage_Percent",
                "Memory_Usage_MB",
                "Disk_Usage_Percent",
                "Health_Status"
            ]
        ].head(20),
        use_container_width=True
    )

    # ---------- JAVASCRIPT ----------
    components.html("""
    <script>
        console.log("Monitoring Page Loaded");
        alert("Live Monitoring Dashboard Activated!");
    </script>
    """, height=0)