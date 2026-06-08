import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="PredictOps AI",
    page_icon="🚀",
    layout="wide")
# custom styling

st.markdown("""
<style>
[data-testid="metric-container"]{
    border:1px solid #ddd;
    padding:15px;
    border-radius:12px;
    box-shadow:0 2px 6px rgba(0,0,0,0.1);}

.main > div {
    padding-top: 1rem;
}
</style>
""", unsafe_allow_html=True)
#side bar

st.sidebar.title("🚀 PredictOps AI")
st.markdown("""
### AI-Powered Server Monitoring & Failure Prediction
Monitor server health, detect anomalies, predict failures, and receive AI recommendations.
""")

from pages.dashboard import show_dashboard
from pages.monitoring import show_monitoring
from pages.failure_prediction import show_prediction
from pages.rf_insights import show_rf_insights
from pages.recommendations import show_recommendations
from pages.model_comparison import show_model

from utils.data_loader import load_data
from utils.model_loader import load_model

try:
    df = load_data()
except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()

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

df["Predicted_Failure"] = model.predict(X)
X = X[model.feature_names_in_]

df["Predicted_Failure"] = model.predict(X)


st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page",
    ["Dashboard", 
     "Monitoring",
     "Failure Prediction",
     "RF Insights",
     "Recommendations",
     "model_comparision"])
       
if page == "Dashboard":
    show_dashboard(df)

elif page == "Monitoring":
    show_monitoring(df)

elif page == "Failure Prediction":
    show_prediction(df)

elif page == "RF Insights":
    show_rf_insights(df)

elif page == "Recommendations":
    show_recommendations(df)

elif page == "model_comparision":
    show_model(df)




