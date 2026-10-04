# test_model.py
# Membrane degradation model test

import joblib
import numpy as np

# Load the model
model = joblib.load("membrane_decay_model.pkl")

# Sample test data
test_data = np.array([
    [3.05, 96.5],
    [3.10, 95.0],
    [3.15, 93.5],
    [3.20, 92.0],
])

# Prediction
predictions = model.predict(test_data)

# Display the result
for i, pred in enumerate(predictions):
    print(f"Sample {i+1}: predicted efficiency = {pred:.2f}")

print("Model test completed successfully.")
