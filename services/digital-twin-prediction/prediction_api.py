# prediction_api.py
# Prediction output interface

import joblib
import numpy as np

# Load the saved model
model = joblib.load("membrane_decay_model.pkl")

def predict(cell_voltage, current_efficiency):
    """
    Predict the membrane degradation trend.
    
    Input:
        cell_voltage: cell voltage
        current_efficiency: current efficiency
    
    Output:
        Predict future current efficiency
    """
    features = np.array([[cell_voltage, current_efficiency]])
    prediction = model.predict(features)
    
    return {
        "predicted_efficiency": float(prediction[0]),
        "confidence_interval": [float(prediction[0] - 0.5), float(prediction[0] + 0.5)],
    }

if __name__ == "__main__":
    result = predict(3.05, 96.5)
    print("Prediction:", result)
