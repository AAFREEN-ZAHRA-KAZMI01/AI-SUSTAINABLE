import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def run():
    st.header("📱 Lite Mobile Dashboard")
    st.write("Explore key metrics in a mobile-friendly layout.")

    # Simulated mobile-style sidebar menu
    with st.sidebar:
        choice = option_menu(
            "Mobile Menu",
            ["Home", "Score", "Usage", "Badge"],
            icons=["house", "star", "bar-chart", "award"],
            menu_icon="cast",
            default_index=0,
            orientation="vertical"
        )

    if choice == "Home":
        st.title("Welcome to Mobile View")
        st.write("Use the side menu to explore performance.")

    elif choice == "Score":
        st.subheader("📊 Daily Energy Score")
        scores = np.random.randint(50, 100, size=7)
        days = pd.date_range(end=pd.Timestamp.today(), periods=7).strftime('%A')
        df = pd.DataFrame({'Day': days, 'Score': scores})
        st.bar_chart(df.set_index('Day'))

    elif choice == "Usage":
        st.subheader("🔌 Energy Usage Summary")
        df = pd.DataFrame({
            'Device': ['AC', 'Printer', 'Lights', 'Fan'],
            'Hours Used': [4, 1, 8, 6],
            'Energy (kWh)': [6.0, 0.8, 2.4, 1.2]
        })
        st.dataframe(df, use_container_width=True)

    elif choice == "Badge":
        st.subheader("🏆 Your Badges")
        st.markdown("""
        - 🌟 **Zero-Waste Wednesday**
        - ⚡ **Efficiency Streak: 5 Days**
        - 🧠 **Smart Scheduler Award**
        """)

    st.markdown("---")
    st.caption("Optimized for mobile-style interaction using Streamlit.")
