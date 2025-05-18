
import streamlit as st
import pandas as pd
import numpy as np

def run():
    st.header('Energy Budgeting Feature')
    st.write('Set daily energy target and see optimized machine schedules.')

    energy_target = st.number_input('Enter your daily energy budget (kWh):', min_value=100, max_value=2000, value=500, step=50)
    st.write(f'Your target daily energy budget is {energy_target} kWh.')

    # Simulate energy consumption of 3 machines with adjustable operation hours
    machines = ['Machine A', 'Machine B', 'Machine C']
    base_consumption = {'Machine A': 200, 'Machine B': 150, 'Machine C': 100}  # kWh per full day operation
    operation_hours = {m: st.slider(f'Operating hours for {m}', 0, 24, 8) for m in machines}

    # Calculate total energy usage
    total_energy = sum(base_consumption[m] * (operation_hours[m] / 24) for m in machines)
    st.write(f'Total estimated energy consumption: {total_energy:.2f} kWh')

    if total_energy > energy_target:
        st.warning('Warning: Energy consumption exceeds your budget! Consider reducing operation hours.')
    else:
        st.success('Good! Your energy consumption is within the budget.')
