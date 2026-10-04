# quality_link_model.py
# Quality-to-grade link model

import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load synthetic data
df = pd.read_csv("arvand_chain_health_data_10k.csv")

# Features: purity of input materials
X = df[['vcm_purity_percent']].values
# Target: final product quality
y = df['pvc_k_value'].values

# Simple linear regression model
model = LinearRegression()
model.fit(X, y)

# Save the model
joblib.dump(model, "quality_link_model.pkl")

print("Quality link model built and saved.")
