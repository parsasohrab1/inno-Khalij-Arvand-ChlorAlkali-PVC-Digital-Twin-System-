# quality_prediction.py
# Product quality prediction

import joblib
import numpy as np

# Load the quality link model
model = joblib.load("quality_link_model.pkl")

def predict_quality(vcm_purity):
    """
    Predict the final product quality based on the purity of input materials.
    """
    features = np.array([[vcm_purity]])
    prediction = model.predict(features)
    
    return {
        "predicted_k_value": float(prediction[0]),
        "quality_status": "Acceptable" if prediction[0] > 67 else "Needs review",
    }

if __name__ == "__main__":
    result = predict_quality(99.9)
    print("Quality prediction:", result)
