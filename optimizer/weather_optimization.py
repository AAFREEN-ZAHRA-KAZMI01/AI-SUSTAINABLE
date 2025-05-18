
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run():
    st.header('Weather Forecast + Energy Optimization Integration')
    st.write('Simulated 7-day weather forecast and adaptive energy optimization for HVAC.')

    # Simulate dummy weather forecast: sunny, cloudy, rain
    weather_conditions = ['Sunny', 'Cloudy', 'Rain']
    np.random.seed(24)
    forecast = np.random.choice(weather_conditions, size=7, p=[0.5,0.3,0.2])
    days = pd.date_range(start=pd.Timestamp.today(), periods=7).strftime('%a %d-%b')

    df_forecast = pd.DataFrame({'Day': days, 'Weather': forecast})

    st.write('7-Day Weather Forecast:')
    st.table(df_forecast)

    # Simulate energy usage adjustments for HVAC based on weather
    base_energy = 100  # base HVAC energy use kWh
    energy_adj = []
    for w in forecast:
        if w == 'Sunny':
            energy_adj.append(base_energy * 0.9)  # less cooling needed
        elif w == 'Cloudy':
            energy_adj.append(base_energy * 1.0)
        else:  # Rain
            energy_adj.append(base_energy * 1.1)  # more heating needed

    df_energy = pd.DataFrame({'Day': days, 'Adjusted HVAC Energy (kWh)': energy_adj})
    st.line_chart(df_energy.set_index('Day'))

    st.write('Energy usage is adjusted according to weather forecast to optimize consumption.')
