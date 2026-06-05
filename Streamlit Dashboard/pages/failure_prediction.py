import streamlit as st
from utils.model_loader import load_model


#risk categories
def risk_level(prob):

    if prob >= 0.8:
        return "Critical"

    elif prob >= 0.5:
        return "Warning"

    else:
        return "Healthy"
def show_prediction(df):
    st.title(
        "🔮 Failure Prediction")
    st.markdown(
    "Predict server failure risk using Random Forest Machine Learning.")
    # Load Model
    try:
        model = load_model()
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return
    features = [ "CPU_Usage_Percent",
            "Memory_Usage_MB",
            "Disk_Usage_Percent",
            "Response_Time_ms",
            "Failed_Transactions",
            "Alert_Count",
            "Error_Count",
            "Retry_Count",
            "Escalation_Level"]
    X = df[features]

    df["Failure_Probability"] = model.predict_proba(X)[:,1]

    df["Risk_Level"] = (
    df["Failure_Probability"]
    .apply(risk_level))
    #overall risk score
    avg_risk = round(
    df["Failure_Probability"].mean() * 100,2)

    st.metric(
    "Overall Failure Risk %",
    avg_risk)


    top_risk = df.sort_values(
    "Failure_Probability",
    ascending=False).head(10)

    st.subheader("🚨 Top Risk Records")

    st.dataframe(
    top_risk[
        [
            "Anomaly_ID",
            "Failure_Probability",
            "Risk_Level"
        ]
    ]
)
    

    import plotly.express as px

    fig = px.bar(
    top_risk,
    x="Anomaly_ID",
    y="Failure_Probability",
    color="Risk_Level",
    title="Top Failure Risk Records"
)

    st.plotly_chart(
    fig,
    use_container_width=True
)

    fig = px.histogram(
    df,
    x="Failure_Probability",
    nbins=20,
    title="Failure Probability Distribution"
)

    st.plotly_chart(
    fig,
    use_container_width=True
)

    st.subheader("📊 Risk Summary")

    st.write(
    df["Risk_Level"].value_counts()
)

    


    