import streamlit as st
import pandas as pd
import joblib

def run():
    st.title("🏭 AI-Powered Phantom Load Detector")

    # Load model
    model = joblib.load("model/phantom_model.pkl")
    features = joblib.load("model/phantom_model_features.pkl")

    # User input
    st.sidebar.header("Enter Machine Info")
    process = st.sidebar.selectbox("Process Type", ['Dyeing', 'Weaving', 'Spinning', 'Finishing'])
    occupancy = st.sidebar.slider("Occupancy (%)", 0, 100, 30)
    machines_active = st.sidebar.slider("Machines Active", 0, 30, 10)
    external_temp = st.sidebar.number_input("External Temp (°C)", 0.0, 50.0, 30.0)
    solar = st.sidebar.selectbox("Solar Available", ['High', 'Low', 'None'])
    efficiency = st.sidebar.slider("Machine Efficiency", 0.0, 1.0, 0.75)
    hour = st.sidebar.slider("Hour", 0, 23, 14)

    input_df = pd.DataFrame({
        'process_type': [process],
        'occupancy': [occupancy],
        'machines_active': [machines_active],
        'external_temp': [external_temp],
        'solar_available': [solar],
        'machine_efficiency': [efficiency],
        'hour': [hour]
    })
    input_df = pd.get_dummies(input_df).reindex(columns=features, fill_value=0)

    if st.button("Detect Phantom Load"):
        result = model.predict(input_df)[0]
        if result:
            st.error("⚠️ Phantom Load Detected! Consider shutdown or scheduling change.")
        else:
            st.success("✅ No Phantom Load Detected. Setup is efficient.")
