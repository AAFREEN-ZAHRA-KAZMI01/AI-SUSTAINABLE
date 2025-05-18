
import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import os

def run():
    st.title("🧠 AI Waste Predictor + Smart Dashboard")
    st.markdown("This tool predicts energy waste and gives insights, badges, and visual feedback.")

    st.sidebar.header("🔧 Enter Machine Info")
    machine_name = st.sidebar.selectbox("Select Machine", ['Weaving', 'Dyeing', 'Spinning'])
    daily_hours = st.sidebar.slider("Daily Usage (hours)", 0, 24, 8)
    num_days = st.sidebar.slider("How many days?", 1, 7, 3)
    occupancy = st.sidebar.slider("Average Occupancy (%)", 0, 100, 40)
    equipment_age = st.sidebar.slider("Equipment Age (years)", 0, 20, 6)
    machine_eff = st.sidebar.slider("Machine Efficiency", 0.0, 1.0, 0.7)
    hour = st.sidebar.slider("Typical Start Hour", 0, 23, 10)

    st.subheader("📋 Input Summary")
    st.markdown(f"**Machine**: {machine_name} | **Used**: {daily_hours}h/day × {num_days} days")
    st.markdown(f"**Occupancy**: {occupancy}% | **Age**: {equipment_age} yrs | **Efficiency**: {machine_eff}")

    if st.button("🔍 Predict & Analyze"):
        model = joblib.load("model/energy_waste_model.pkl")
        features = joblib.load("model/model_features.pkl")

        input_df = pd.DataFrame({
            'occupancy': [occupancy],
            'equipment_age': [equipment_age],
            'machine_efficiency': [machine_eff],
            'hour': [hour]
        })
        for p in ['Weaving', 'Dyeing', 'Spinning']:
            input_df[f'process_type_{p}'] = 1 if p == machine_name else 0
        input_df = input_df.reindex(columns=features, fill_value=0)

        prediction = model.predict(input_df)[0]
        result = '⚠️ Waste Likely ❌' if prediction == 1 else '✅ Efficient Setup 👍'
        st.success(f"### {result}")

        # Save to CSV
        save_row = input_df.copy()
        save_row['machine_name'] = machine_name
        save_row['prediction'] = prediction
        csv_path = "optimizer/user_predictions.csv"
        if os.path.exists(csv_path):
            past = pd.read_csv(csv_path)
            updated = pd.concat([past, save_row], ignore_index=True)
        else:
            updated = save_row
        updated.to_csv(csv_path, index=False)
        st.info("✅ Your prediction was saved for future analysis.")

        # Display badge
        if prediction == 0:
            st.balloons()
            st.markdown("🏆 **Badge Unlocked:** Energy Hero - Efficient Setup!")
        else:
            st.markdown("💡 Try reducing equipment age or scheduling more efficient hours.")

        # Graph: Estimated energy over the week
        hours_series = [daily_hours * machine_eff] * num_days
        days = [f"Day {i+1}" for i in range(num_days)]
        st.subheader("📈 Estimated Energy Curve")
        fig, ax = plt.subplots()
        ax.plot(days, hours_series, marker='o', color='green' if prediction == 0 else 'red')
        ax.set_ylabel("Estimated kWh Used")
        ax.set_title("Energy Usage Over Days")
        st.pyplot(fig)
