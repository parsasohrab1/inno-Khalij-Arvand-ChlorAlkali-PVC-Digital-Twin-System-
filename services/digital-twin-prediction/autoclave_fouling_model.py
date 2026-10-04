# autoclave_fouling_model.py
# Autoclave fouling prediction model

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Load synthetic data
df = pd.read_csv("arvand_chain_health_data_10k.csv")

# Features: heat transfer coefficient and agitator power
X = df[['jacket_heat_transfer_coeff', 'agitator_motor_power_kw']].values
# Target: fouling index (inverse of heat transfer coefficient)
y = df['jacket_heat_transfer_coeff'].values

# Simple linear regression model
model = LinearRegression()
model.fit(X, y)

# Save the model
joblib.dump(model, "autoclave_fouling_model.pkl")

print("Autoclave fouling model built and saved.")
