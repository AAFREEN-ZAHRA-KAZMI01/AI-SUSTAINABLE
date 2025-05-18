import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def run():
    st.header("🌱 Sustainability Meter (Gamification + Motivation)")
    st.write("""
    Track your daily energy efficiency score and earn badges for consistent good habits!
    """)

    # Simulate daily energy scores for past 14 days (0 to 100)
    np.random.seed(42)
    days = [datetime.today() - timedelta(days=i) for i in range(13, -1, -1)]
    scores = np.random.randint(50, 100, size=14)  # Random scores between 50 and 100

    df = pd.DataFrame({
        'Date': [d.strftime('%Y-%m-%d') for d in days],
        'Energy Efficiency Score': scores
    })

    # Display scores as line chart
    st.line_chart(df.set_index('Date')['Energy Efficiency Score'])

    # Calculate badges
    badges = []
    for idx, row in df.iterrows():
        score = row['Energy Efficiency Score']
        if score >= 90:
            badges.append('🌟 Zero-Waste Wednesday' if idx % 7 == 2 else '⚡ Efficiency Star')
        elif score >= 75:
            badges.append('👍 Good Day')
        else:
            badges.append('⚠️ Needs Improvement')

    df['Badge'] = badges

    st.subheader("Weekly Dashboard with Badges")
    st.dataframe(df)

    # Calculate efficiency streaks (days with score >= 75)
    streak = 0
    max_streak = 0
    for score in scores:
        if score >= 75:
            streak += 1
            max_streak = max(max_streak, streak)
        else:
            streak = 0

    st.markdown(f"### ⚡ Efficiency Streak: {max_streak} days")

    st.markdown("""
    #### How to improve your score:
    - Reduce unnecessary energy usage.
    - Turn off devices when not in use.
    - Use energy-efficient appliances.
    - Shift energy-heavy tasks to off-peak hours.
    """)

