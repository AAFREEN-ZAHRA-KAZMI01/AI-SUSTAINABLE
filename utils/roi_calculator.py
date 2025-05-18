def calculate_roi(estimated_savings_per_month, ai_system_cost):
    if ai_system_cost == 0:
        return float('inf')
    months_to_recover = ai_system_cost / estimated_savings_per_month
    return round(months_to_recover, 2)