# cell_health_connection.py
# اتصال مدل کیفیت به سلامت سلول بالادستی

import joblib
import numpy as np

# بارگذاری مدل کیفیت
quality_model = joblib.load("quality_link_model.pkl")

def predict_quality_from_cell_health(cell_voltage, current_efficiency):
    """
    پیش‌بینی کیفیت محصول بر اساس سلامت سلول بالادستی.
    """
    # رابطه ساده: خلوص VCM به راندمان جریان بستگی دارد.
    # این رابطه نمونه است و باید با داده واقعی کالیبره شود.
    vcm_purity = 99.9 - 0.02 * (100 - current_efficiency) / 8
    features = np.array([[vcm_purity]])
    prediction = quality_model.predict(features)
    return {
        "predicted_k_value": float(prediction[0]),
        "quality_status": "قابل قبول" if prediction[0] > 67 else "نیاز به بررسی",
    }

if __name__ == "__main__":
    result = predict_quality_from_cell_health(3.05, 96.5)
    print("پیش‌بینی کیفیت از سلامت سلول:", result)
