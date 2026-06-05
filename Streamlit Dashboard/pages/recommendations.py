import streamlit as st
from utils.model_loader import load_model


def get_recommendation(row):

    if row["CPU_Usage_Percent"] > 90:
        return "Increase CPU Resources"

    elif row["Memory_Usage_MB"] > 40000:
        return "Increase RAM Capacity"

    elif row["Disk_Usage_Percent"] > 90:
        return "Clean Disk Space"

    elif row["Error_Count"] > 100:
        return "Investigate Application Logs"

    else:
        return "No Action Needed"


def show_recommendations(df):

    st.title("🤖 AI Recommendations")
    st.write("Preventive Actions")

    try:
        model = load_model()
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return

    features = [
        "CPU_Usage_Percent",
        "Memory_Usage_MB",
        "Disk_Usage_Percent",
        "Response_Time_ms",
        "Failed_Transactions",
        "Alert_Count",
        "Error_Count",
        "Retry_Count",
        "Escalation_Level"
    ]

    X = df[features]

    df["Failure_Probability"] = (
        model.predict_proba(X)[:, 1]
    )

    df["Recommendation"] = (
        df.apply(
            get_recommendation,
            axis=1
        )
    )

    high_risk = df[
        df["Failure_Probability"] > 0.8
    ]

    st.subheader("High Risk Servers")

    st.dataframe(
        high_risk[
            [
                "Anomaly_ID",
                "Failure_Probability",
                "Recommendation"
            ]
        ]
    )

    st.success(
        f"Total High-Risk Servers: {len(high_risk)}"
    )