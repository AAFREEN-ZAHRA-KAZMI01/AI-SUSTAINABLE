import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from optimizer import dashboard, self_learning_ai, weather_optimization, energy_budgeting, predictive_scheduling,phantom_load_detector,roi_calculator,sustainability_meter,explainable_ai,problem3_energy_optimizer
from optimizer import problem3_energy_optimizer
from optimizer import lite_mobile_dashboard,ml_energy_waste_predictor



def main():
    st.set_page_config(page_title='Textile Energy Optimization', layout='wide')
    st.sidebar.title("Navigation")
    menu = ['Home', 'Dashboard', 'Self-Learning AI', 'Weather & Energy Optimization', 'Energy Budgeting', 'Predictive Scheduling','Phantom Load Detector','ROI Calculator', 'Sustainability Meter','Explainable AI Dashboard','Lite Mobile Dashboard','AI Waste Predictor','Problem-3 Optimizer']
    choice = st.sidebar.selectbox('Go to', menu)

    if choice == 'Home':
        st.title('Welcome to Textile Energy Optimization Project')
        st.write("""
        This project helps optimize energy usage in the textile industry using AI-driven analytics and smart recommendations.

        Use the sidebar to navigate through different modules:
        - **Dashboard:** Explore energy data and recommendations.
        - **Self-Learning AI:** Adaptive weekly optimization.
        - **Weather & Energy Optimization:** Adjust energy based on weather forecasts.
        - **Energy Budgeting:** Set daily energy targets and optimize.
        - **Predictive Scheduling:** Auto-generate weekly machine schedules.
        """)

    elif choice == 'Dashboard':
        dashboard.run()

    elif choice == 'Self-Learning AI':
        self_learning_ai.run()

    elif choice == 'Weather & Energy Optimization':
        weather_optimization.run()

    elif choice == 'Energy Budgeting':
        energy_budgeting.run()

    elif choice == 'Predictive Scheduling':
        predictive_scheduling.run()
   
    elif choice == 'Phantom Load Detector':
         phantom_load_detector.run()
    elif choice == 'ROI Calculator':
        roi_calculator.run()
    elif choice == 'Sustainability Meter':
        sustainability_meter.run()
    elif choice == 'Explainable AI Dashboard':
        explainable_ai.run()
    elif choice == 'Lite Mobile Dashboard':
        lite_mobile_dashboard.run()
    elif choice == "AI Waste Predictor":
         ml_energy_waste_predictor.run()
    elif choice == "Problem-3 Optimizer":
        problem3_energy_optimizer.run()

     


if __name__ == '__main__':
    main()


