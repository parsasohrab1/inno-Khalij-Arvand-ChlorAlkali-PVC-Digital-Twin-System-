# autoclave_fouling_model.py
# مدل پیش‌بینی فولینگ اتوکلاو

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# بارگذاری داده سنتتیک
df = pd.read_csv("arvand_chain_health_data_10k.csv")

# ویژگی‌ها: ضریب انتقال حرارت و توان همزن
X = df[['jacket_heat_transfer_coeff', 'agitator_motor_power_kw']].values
# هدف: شاخص فولینگ (برعکس ضریب انتقال حرارت)
y = df['jacket_heat_transfer_coeff'].values

# مدل ساده رگرسیون خطی
model = LinearRegression()
model.fit(X, y)

# ذخیره مدل
joblib.dump(model, "autoclave_fouling_model.pkl")

print("مدل فولینگ اتوکلاو ساخته و ذخیره شد.")
