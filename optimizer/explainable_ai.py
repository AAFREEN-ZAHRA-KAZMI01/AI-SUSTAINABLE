import streamlit as st
import pandas as pd

def run():
    st.header("🧭 Explainable AI Dashboard (XAI)")
    st.write("""
    Understand the reasons behind AI recommendations with detailed explanations and metrics.
    """)

    # Sample data simulating AI recommendations with explanations
    data = {
        'Machine': ['Machine A', 'Machine B', 'Machine C', 'Machine D'],
        'Recommendation': [
            'Turn OFF at 2 AM',
            'Run only 9 AM–5 PM',
            'Reduce speed during night shifts',
            'Schedule maintenance this week'
        ],
        'Explanation': [
            'Occupancy = 0 at 2 AM and previous energy waste = 30%',
            'Low occupancy in early mornings; optimize runtime to save energy',
            'Night shift energy consumption spikes; reduce speed to save 15%',
            'Motor vibration above threshold; recommended maintenance to prevent failure'
        ],
        'Confidence Score (%)': [95, 88, 80, 92]
    }

    df = pd.DataFrame(data)

    # Show recommendations table
    st.subheader("AI Recommendations with Explanations")
    st.dataframe(df)

    # Filter by confidence score
    threshold = st.slider("Minimum Confidence Score (%) to display:", 0, 100, 75)
    filtered_df = df[df['Confidence Score (%)'] >= threshold]

    st.subheader(f"Filtered Recommendations (Confidence ≥ {threshold}%)")
    st.dataframe(filtered_df)

    st.markdown("""
    ---
    **Note:** This dashboard helps operators understand AI decisions clearly, improving trust and adoption.
    """)

