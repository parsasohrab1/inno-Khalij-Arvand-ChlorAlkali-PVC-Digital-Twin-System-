# prediction_api.py
# رابط خروجی پیش‌بینی

import joblib
import numpy as np

# بارگذاری مدل ذخیره‌شده
model = joblib.load("membrane_decay_model.pkl")

def predict(cell_voltage, current_efficiency):
    """
    پیش‌بینی روند زوال غشا.
    
    ورودی:
        cell_voltage: ولتاژ سلول
        current_efficiency: راندمان جریان
    
    خروجی:
        پیش‌بینی راندمان جریان آینده
    """
    features = np.array([[cell_voltage, current_efficiency]])
    prediction = model.predict(features)
    
    return {
        "predicted_efficiency": float(prediction[0]),
        "confidence_interval": [float(prediction[0] - 0.5), float(prediction[0] + 0.5)],
    }

if __name__ == "__main__":
    result = predict(3.05, 96.5)
    print("پیش‌بینی:", result)
