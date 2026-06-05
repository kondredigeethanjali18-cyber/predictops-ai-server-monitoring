import joblib
import streamlit as st

@st.cache_resource
def load_model():
    return joblib.load(
        "Streamlit Dashboard/random_forest_model.pkl"
    )
