# 🧠 Smart AI-Based Energy Optimization System for the Textile Industry

## 📌 Project Overview

This AI-powered system is designed to optimize energy consumption in textile manufacturing facilities by detecting energy waste, forecasting phantom loads, and suggesting intelligent operational adjustments. Using real-time or simulated data, it enhances energy efficiency and cost savings while supporting sustainability goals.

---

## 🔍 Key Features

- 🔎 **Energy Waste Detection**: Identify inefficient energy usage based on thresholds and production status.
- ⚡ **Phantom Load Prediction**: Detect idle energy consumption during non-operational hours.
- 🎯 **Energy Budgeting Module**: Maintain daily or weekly energy use under defined limits.
- 🌞 **Renewable Energy Prioritization**: Shift operations to periods of solar availability.
- 🛠️ **Predictive Maintenance Alerts**: Warns about faults based on abnormal power draw patterns.
- 📊 **Interactive Dashboard**: Streamlit-based UI for visualizing energy trends, savings, and alerts.

---

## 🏭 Target Industry Use Case: Textile Manufacturing

In a typical textile facility, energy is consumed across four major domains:

1. **Spinning**: High-speed machinery requires continuous optimization.
2. **Weaving**: Power looms have fluctuating demands based on textile types.
3. **Dyeing & Finishing**: Thermal energy losses are common during these processes.
4. **Utilities (HVAC, Lighting, Compressors)**: Often responsible for hidden phantom loads.

---

## 🧑‍💻 Technologies Used

- **Language**: Python
- **Libraries**: `pandas`, `scikit-learn`, `matplotlib`, `joblib`, `streamlit`
- **Model**: Random Forest Classifier
- **Visualization**: Streamlit
- **Data Input**: CSV files / simulated sensor logs

---

## 🧪 System Modules

| Module | Description |
|--------|-------------|
| **1. Data Ingestion & Preprocessing** | Load, clean, and process energy & machine usage data |
| **2. Waste Detection** | Predict and label energy waste using Random Forest |
| **3. Phantom Load Prediction** | Classify idle power consumption patterns |
| **4. Energy Budgeting** | Manage and optimize toward user-defined energy targets |
| **5. Renewable Optimization** | Shift energy use to renewable availability windows |
| **6. Maintenance Alerts** | Fault detection using anomaly-based thresholds |
| **7. Streamlit Dashboard** | Real-time visualization, trends, alerts, and savings |

---

## 📈 Sample Results

| Metric | Before Optimization | After Optimization |
|--------|----------------------|---------------------|
| Energy Waste | 18% | 6% |
| Phantom Load | 15% | 3% |
| Budget Target Met | 4/7 days | 6/7 days |

---

## 🧩 Your Contribution (Author Notes)

> 🔧 Developed data preprocessing pipeline for textile energy logs  
> 🔧 Simulated phantom loads using historical HVAC & machine data  
> 🔧 Trained and evaluated Random Forest models on efficiency thresholds  
> 🔧 Built Streamlit dashboard with real-time alerts and graphs  
> 🔧 Created logic for 7-day budget tracking system  

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/your-username/energy-optimizer-textile.git
cd energy-optimizer-textile

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py


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
