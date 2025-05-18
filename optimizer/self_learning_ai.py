
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run():
    st.header('Self-Learning AI (Adaptive Optimization)')
    st.write('This module learns weekly patterns and adapts optimization accordingly.')

    # Simulate weekly data for 3 machines (energy usage by hour)
    np.random.seed(42)
    hours = list(range(24))
    machines = ['Machine A', 'Machine B', 'Machine C']

    st.write('Simulated weekly energy usage data (average by hour):')
    data = {m: np.random.normal(50 + 10 * np.sin((np.array(hours) + i*3)/24 * 2 * np.pi), 5, 24) for i, m in enumerate(machines)}
    df = pd.DataFrame(data, index=hours)
    st.line_chart(df)

    # Simple "learning" logic: find machine with max usage morning (6-12) vs evening (18-24)
    morning_hours = list(range(6,13))
    evening_hours = list(range(18,24))

    morning_avg = df.loc[morning_hours].mean()
    evening_avg = df.loc[evening_hours].mean()

    st.write('Average energy usage in morning hours (6 AM - 12 PM):')
    st.write(morning_avg)

    st.write('Average energy usage in evening hours (6 PM - 12 AM):')
    st.write(evening_avg)

    # Determine efficiency pattern
    patterns = []
    for m in machines:
        if morning_avg[m] > evening_avg[m]:
            patterns.append(f"{m} is more efficient in the morning.")
        else:
            patterns.append(f"{m} is more efficient in the evening.")

    st.success('AI Learned Patterns:')
    for p in patterns:
        st.write(f"- {p}")
