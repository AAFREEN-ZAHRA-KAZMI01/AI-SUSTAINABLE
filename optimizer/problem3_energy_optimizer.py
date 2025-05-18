
import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

def run():
    st.title("⚡ Problem-3: AI-Based Energy Optimization")

    st.markdown("""
    ### 📌 Simulation Assumptions
    - Factory shift usage = 30–50 kWh/hour.
    - Above 20 kWh/hour is considered inefficient for real data.
    - HVAC suggestions based on forecast & occupancy.
    - AI optimizer simulates 20% energy reduction on inefficiencies.
    - Summary insights help justify recommendations with estimated savings.
    """)

    uploaded = st.file_uploader("📁 Upload dataset (p3.csv or textile_energy_data.csv)", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)

        # Normalize columns
        if "Total Consumption (kWh)" in df.columns:
            df.rename(columns={"Total Consumption (kWh)": "energy_kwh", "Timestamp": "timestamp"}, inplace=True)
        elif "energy_used_kwh" in df.columns:
            df.rename(columns={"energy_used_kwh": "energy_kwh"}, inplace=True)
            if 'timestamp' not in df.columns and 'Timestamp' in df.columns:
                df.rename(columns={"Timestamp": "timestamp"}, inplace=True)

        if 'timestamp' not in df.columns:
            st.error("❌ Missing 'timestamp' column.")
            return

        # Time features
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
        df.dropna(subset=['timestamp'], inplace=True)
        df['hour'] = df['timestamp'].dt.hour
        df['day'] = df['timestamp'].dt.day

        # Simulate missing data
        if 'occupancy' not in df.columns:
            df['occupancy'] = 30
        if 'HVAC (kWh)' not in df.columns:
            df['HVAC (kWh)'] = df['energy_kwh'] * 0.15
        if 'forecast' not in df.columns:
            df['forecast'] = 'Clear'

        # Load model
        try:
            model = joblib.load("model/efficiency_model.pkl")
            features = joblib.load("model/efficiency_model_features.pkl")
            df['inefficiency_prediction'] = model.predict(df[features])
        except:
            df['inefficiency_prediction'] = (df['energy_kwh'] > 50).astype(int)

        # Manual override if model gives all 0
        if df['inefficiency_prediction'].sum() == 0:
            df['inefficiency_prediction'] = (df['energy_kwh'] > 20).astype(int)

        # Recommendations
        def get_tip(row):
            tips = []
            if row['inefficiency_prediction'] == 1:
                if row['hour'] > 20:
                    tips.append("⚠️ Shift usage to daytime")
                else:
                    tips.append("🔧 Reschedule or reduce load")
            if row['occupancy'] < 20 and row['HVAC (kWh)'] > 10:
                tips.append("🌬️ Reduce HVAC — low occupancy")
            if row['forecast'].lower() == 'rain':
                tips.append("🌧️ Increase HVAC — rain expected")
            elif row['forecast'].lower() == 'clear':
                tips.append("☀️ Reduce HVAC — sunny")
            return ' | '.join(tips) if tips else "✅ Normal usage"

        df['recommendation'] = df.apply(get_tip, axis=1)

        # Optimization logic
        df['optimized_kwh'] = df.apply(
            lambda row: row['energy_kwh'] * 0.8 if row['inefficiency_prediction'] == 1 else row['energy_kwh'], axis=1
        )

        # Show predictions
        st.subheader("🔍 AI Recommendations")
        st.dataframe(df[['timestamp', 'energy_kwh', 'inefficiency_prediction', 'recommendation', 'optimized_kwh']].head(25))

        # Chart
        st.subheader("📊 Baseline vs Optimized")
        chart_df = df[['timestamp', 'energy_kwh', 'optimized_kwh']].set_index('timestamp')
        st.line_chart(chart_df)

        # Summary metrics
        total_before = df['energy_kwh'].sum()
        total_after = df['optimized_kwh'].sum()
        total_saved = total_before - total_after

        st.metric("⚡ Energy Before", f"{total_before:.2f} kWh")
        st.metric("🌿 After Optimization", f"{total_after:.2f} kWh")
        st.success(f"✅ Estimated Energy Saved: {total_saved:.2f} kWh")

        # Summary Insight Example
        st.subheader("📋 AI Insight Summary")
        idle_hours = df[df['hour'].between(0, 5)]
        idle_total = idle_hours['energy_kwh'].sum()
        idle_percent = (idle_total / df['energy_kwh'].sum()) * 100
        night_savings = idle_total * 0.4  # assume 40% can be reduced

        st.markdown(f"""
        **🧠 Insight:** {idle_percent:.1f}% of your factory's energy is consumed during the night (12 AM–5 AM).

        **📉 Action:** AI recommends scheduling machine shutdowns during these hours.

        **💰 Estimated Saving:** ~{night_savings:.2f} kWh/month
        """)
