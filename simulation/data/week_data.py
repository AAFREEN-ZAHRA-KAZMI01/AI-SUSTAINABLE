import os
import pandas as pd

# Data folder path (adjust karen apne project structure ke mutabiq)
data_folder = 'data/weekly_data'
os.makedirs(data_folder, exist_ok=True)

# Sample weekly data dictionary
data = {
    'timestamp': [
        '2025-05-01 08:00:00', '2025-05-01 09:00:00', '2025-05-01 10:00:00',
        '2025-05-01 11:00:00', '2025-05-01 12:00:00', '2025-05-01 13:00:00',
        '2025-05-01 14:00:00', '2025-05-01 15:00:00'
    ],
    'process_type': [
        'Spinning', 'Spinning', 'Weaving', 'Weaving', 'Dyeing', 'Dyeing', 'Finishing', 'Finishing'
    ],
    'occupancy': [75, 80, 60, 55, 40, 35, 50, 45],
    'machines_active': [10, 11, 8, 9, 7, 6, 5, 5],
    'external_temp': [30, 30, 32, 33, 35, 36, 34, 33],
    'solar_available': ['High', 'High', 'Low', 'Low', 'None', 'None', 'Low', 'Low'],
    'energy_used_kwh': [50, 52, 45, 47, 40, 38, 30, 29],
    'idle_energy_kwh': [5, 4, 3, 2, 6, 5, 3, 3],
    'equipment_age': [5, 5, 6, 6, 9, 9, 4, 4],
    'phantom_load': [False, False, False, False, False, False, False, False],
    'forecast': ['Clear', 'Clear', 'Clear', 'Clear', 'Clear', 'Clear', 'Clear', 'Clear'],
    'machine_efficiency': [0.85, 0.87, 0.90, 0.88, 0.70, 0.72, 0.95, 0.93],
    'ai_recommendation': ['', '', '', '', '', '', '', ''],
    'waste_reason': [
        'Low occupancy', 'Low occupancy', 'Old machine', 'Old machine',
        'HVAC misuse', 'HVAC misuse', 'Low occupancy', 'Low occupancy'
    ]
}

# Create DataFrame
df_week = pd.DataFrame(data)

# Save to CSV
file_path = os.path.join(data_folder, 'week_1_sample.csv')
df_week.to_csv(file_path, index=False)
print(f"✅ Sample weekly data saved to {file_path}")
py