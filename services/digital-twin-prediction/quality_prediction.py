# quality_prediction.py
# پیش‌بینی کیفیت محصول

import joblib
import numpy as np

# بارگذاری مدل پیوند کیفیت
model = joblib.load("quality_link_model.pkl")

def predict_quality(vcm_purity):
    """
    پیش‌بینی کیفیت محصول نهایی بر اساس خلوص مواد ورودی.
    """
    features = np.array([[vcm_purity]])
    prediction = model.predict(features)
    
    return {
        "predicted_k_value": float(prediction[0]),
        "quality_status": "قابل قبول" if prediction[0] > 67 else "نیاز به بررسی",
    }

if __name__ == "__main__":
    result = predict_quality(99.9)
    print("پیش‌بینی کیفیت:", result)
