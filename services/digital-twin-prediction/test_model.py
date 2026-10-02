# test_model.py
# تست مدل زوال غشا

import joblib
import numpy as np

# بارگذاری مدل
model = joblib.load("membrane_decay_model.pkl")

# داده تست نمونه
test_data = np.array([
    [3.05, 96.5],
    [3.10, 95.0],
    [3.15, 93.5],
    [3.20, 92.0],
])

# پیش‌بینی
predictions = model.predict(test_data)

# نمایش نتیجه
for i, pred in enumerate(predictions):
    print(f"نمونه {i+1}: راندمان پیش‌بینی‌شده = {pred:.2f}")

print("تست مدل با موفقیت انجام شد.")
