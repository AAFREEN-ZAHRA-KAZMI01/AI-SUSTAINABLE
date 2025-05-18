# Textile Energy Optimization Project

This project simulates textile industry energy usage and provides smart AI-driven recommendations to optimize energy consumption.

## Project Structure
- simulation/: Data generation scripts
- optimizer/: AI optimization and recommendation modules
- utils/: Helper utilities like ROI calculation and weather forecast
- app/: Streamlit dashboard app
- data/: Stores CSV data files

## How to Run
1. Generate synthetic data:
   ```
   python simulation/data_generator.py
   ```
2. Add smart recommendations:
   ```
   python optimizer/optimizer.py
   ```
3. Run Streamlit app:
   ```
   streamlit run app/app.py
   ```