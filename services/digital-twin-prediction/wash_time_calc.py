# wash_time_calc.py
# Optimal washing time calculation

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Load synthetic data
df = pd.read_csv("arvand_chain_health_data_10k.csv")

# Features: heat transfer coefficient and agitator power
X = df[['jacket_heat_transfer_coeff', 'agitator_motor_power_kw']].values
# Target: cycle time (as a measure of washing need)
y = df['batch_cycle_time_min'].values

# Simple linear regression model
model = LinearRegression()
model.fit(X, y)

# Save the model
joblib.dump(model, "wash_time_model.pkl")

# Estimate the approximate time until washing
def estimate_wash_time(heat_transfer_coeff, motor_power):
    # If the heat transfer coefficient drops, washing time is near
    if heat_transfer_coeff < 550:
        return "Immediate washing required"
    elif heat_transfer_coeff < 650:
        return "About 5 days until washing"
    else:
        return "Normal status"

print(estimate_wash_time(500, 125))
print("Washing time calculation completed.")
