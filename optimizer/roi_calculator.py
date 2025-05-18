import streamlit as st

def run():
    st.header("ROI Calculator – Financial Justification Tool")
    st.write("""
    Calculate how fast your energy optimizations will recover the AI deployment cost.
    This helps demonstrate business value clearly.
    """)

    # User inputs
    ai_cost = st.number_input("Enter AI Deployment Cost (in USD):", min_value=0.0, value=10000.0, step=100.0)
    monthly_savings_percent = st.slider("Estimated Monthly Energy Cost Savings (%):", min_value=0, max_value=100, value=15)
    current_monthly_energy_cost = st.number_input("Current Monthly Energy Cost (in USD):", min_value=0.0, value=2000.0, step=100.0)

    # Calculate monthly savings in USD
    monthly_savings = current_monthly_energy_cost * (monthly_savings_percent / 100)

    # Calculate months to recover cost
    if monthly_savings > 0:
        months_to_recover = ai_cost / monthly_savings
        st.success(f"Estimated time to recover AI deployment cost: {months_to_recover:.1f} months")
    else:
        st.warning("Monthly savings must be greater than zero to calculate ROI.")

    # Show summary
    st.markdown(f"""
    **Summary:**
    - AI Deployment Cost: ${ai_cost:,.2f}
    - Estimated Monthly Savings: ${monthly_savings:,.2f} ({monthly_savings_percent}% of current energy cost)
    - Months to Break-Even: {months_to_recover:.1f} months
    """)

    st.info("Use realistic savings estimates based on your optimization results for best accuracy.")
