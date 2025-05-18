import pandas as pd
import numpy as np
import random
from datetime import datetime
import os

# Create 'data' directory if it doesn't exist
os.makedirs("data", exist_ok=True)

# Parameters
days = 30
date_rng = pd.date_range(start='2025-05-01', periods=24*days, freq='h')

process_types = ["Spinning", "Weaving", "Dyeing", "Finishing"]
forecast_options = ["Clear", "Cloudy", "Rain"]
solar_levels = ["High", "Low", "None"]
waste_reasons = ["Old machine", "HVAC misuse", "Low occupancy", "Phantom load"]

data = []

for timestamp in date_rng:
    process = random.choice(process_types)
    occupancy = random.randint(0, 100)
    machines_active = random.randint(2, 20)
    external_temp = random.uniform(20, 45)
    solar_available = random.choice(solar_levels)
    equipment_age = random.randint(1, 10)
    forecast = random.choice(forecast_options)
    phantom = random.choice([True, False])

    # Efficiency drops with age
    machine_efficiency = round(1.0 - (equipment_age * 0.05), 2)

    # Energy used based on multiple factors
    energy_used_kwh = round(
        machines_active * machine_efficiency * (1 + external_temp / 100), 2
    )

    idle_energy_kwh = 0 if occupancy > 20 else round(energy_used_kwh * 0.3, 2)

    ai_recommendation = ""
    if occupancy < 10 and process == "Dyeing":
        ai_recommendation = "Avoid dyeing at low occupancy"
    elif phantom:
        ai_recommendation = "Shutdown idle machines"
    elif equipment_age > 7 and energy_used_kwh > 50:
        ai_recommendation = "Schedule maintenance"

    waste_reason = random.choice(waste_reasons)

    data.append({
        "timestamp": timestamp,
        "process_type": process,
        "occupancy": occupancy,
        "machines_active": machines_active,
        "external_temp": round(external_temp, 2),
        "solar_available": solar_available,
        "energy_used_kwh": energy_used_kwh,
        "idle_energy_kwh": idle_energy_kwh,
        "equipment_age": equipment_age,
        "phantom_load": phantom,
        "forecast": forecast,
        "machine_efficiency": machine_efficiency,
        "ai_recommendation": ai_recommendation,
        "waste_reason": waste_reason
    })

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("data/textile_energy_data.csv", index=False)
print("✅ Dataset generated and saved to 'data/textile_energy_data.csv'")
