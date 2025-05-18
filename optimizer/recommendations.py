def textile_smart_recommendations(row):
    recs = []

    if row['process_type'] == 'Dyeing' and row['solar_available'] != 'High':
        recs.append("Shift heat-intensive dyeing to off-peak solar hours to save cost and utilize solar efficiently.")
    hour = row['timestamp'].hour if hasattr(row['timestamp'], 'hour') else int(str(row['timestamp'])[11:13])
    if row['process_type'] == 'Spinning' and (hour >= 22 or hour < 6):
        recs.append("Shut down spinning machines during night idle shifts to avoid phantom usage.")
    if row['equipment_age'] > 8:
        recs.append("Schedule maintenance for motors older than 8 years as efficiency drops sharply with age.")
    if row['process_type'] == 'Weaving' and row['equipment_age'] <= 5:
        recs.append("Prioritize modern weaving lines during peak hours for higher efficiency and cost saving.")
    if row['forecast'] in ['Clear', 'Cloudy'] and row['external_temp'] > 30:
        recs.append("Use forecast data to schedule HVAC efficiently in summer to reduce overcooling.")
    if row['equipment_age'] > 7 and row['energy_used_kwh'] > 150:
        recs.append("Consider installing inverter-based drives for inefficient old machines.")
    if not recs:
        recs.append("No specific smart recommendations at this time.")
    return recs