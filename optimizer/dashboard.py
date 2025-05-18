import os
import streamlit as st
import pandas as pd

def run():
    st.title("Textile Industry Energy Optimization Dashboard with Smart Recommendations")
    st.write("""
    Welcome to the dashboard! Here you can explore energy usage data, view smart recommendations, 
    and monitor key metrics to optimize your textile industry's energy consumption.
    """)
    
    # Load CSV file from simulation/data folder
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'simulation', 'data'))
    csv_path = os.path.join(base_dir, 'textile_energy_data_with_recommendations.csv')
    
    try:
        df = pd.read_csv(csv_path, parse_dates=['timestamp'])
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return
    
    # Sidebar filters
    st.sidebar.header("Filters")
    process_types = df['process_type'].unique()
    selected_process = st.sidebar.multiselect("Select Process Types", process_types, default=process_types)
    
    filtered = df[df['process_type'].isin(selected_process)]
    
    # Key Metrics
    st.subheader("Key Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Records", len(filtered))
    col2.metric("Average Energy Used (kWh)", f"{filtered['energy_used_kwh'].mean():.2f}")
    col3.metric("Average Occupancy (%)", f"{filtered['occupancy'].mean():.2f}")
    
    # Energy Usage Bar Chart
    st.subheader("Average Energy Usage by Process")
    avg_energy = filtered.groupby('process_type')['energy_used_kwh'].mean().sort_values(ascending=False)
    st.bar_chart(avg_energy)
    
    # Smart Recommendations Logic
    def generate_recommendation(row):
        recs = []
        hour = row['timestamp'].hour
        process = row['process_type']
        occupancy = row['occupancy']
        equipment_age = row['equipment_age']
        energy_used = row['energy_used_kwh']
        forecast = row.get('forecast', None)
        machine_efficiency = row.get('machine_efficiency', None)

        if process == 'Dyeing' and occupancy < 20 and (hour >= 22 or hour < 6):
            recs.append("Shift dyeing to off-peak solar hours for cost savings")

        if process == 'Spinning' and occupancy < 10 and (hour >= 22 or hour < 6):
            recs.append("Shutdown spinning machines during night idle shifts to avoid phantom usage")

        if equipment_age > 8:
            recs.append("Schedule maintenance for motors older than 8 years")

        if process == 'Weaving' and machine_efficiency and machine_efficiency > 0.8:
            recs.append("Prioritize modern weaving lines for peak hours")

        if forecast:
            if forecast.lower() == 'clear':
                recs.append("Schedule HVAC for summer based on clear weather forecast")
            elif forecast.lower() == 'rain':
                recs.append("Adjust HVAC schedule due to rain forecast")

        if equipment_age > 7 and energy_used > 50:
            recs.append("Consider inverter-based drives for energy efficiency")

        if not recs:
            recs.append("No specific recommendation")

        return recs

    # Apply recommendations
    filtered['smart_recommendations'] = filtered.apply(generate_recommendation, axis=1)

    st.subheader("Sample Smart Recommendations")
    sample = filtered[['timestamp', 'process_type', 'energy_used_kwh', 'occupancy', 'equipment_age', 'smart_recommendations']].head(20)
    # Format recommendations as bullet points
    sample['smart_recommendations'] = sample['smart_recommendations'].apply(lambda recs: '\n- '.join(recs))
    st.dataframe(sample)
