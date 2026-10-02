# membrane_decay_model.py
# مدل پیش‌بینی زوال غشا
# این کد نمونه اولیه است و بعداً با داده واقعی تکمیل می‌شود.

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# بارگذاری داده سنتتیک
df = pd.read_csv("arvand_chain_health_data_10k.csv")

# ویژگی‌ها: ولتاژ سلول و راندمان جریان
X = df[['cell_voltage_v', 'current_efficiency_percent']].values
# هدف: شاخص زوال غشا (به عنوان مثال، راندمان جریان آینده)
y = df['current_efficiency_percent'].values

# تقسیم داده
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# مدل ساده رگرسیون خطی
model = LinearRegression()
model.fit(X_train, y_train)

# ذخیره مدل
joblib.dump(model, "membrane_decay_model.pkl")

print("مدل زوال غشا ساخته و ذخیره شد.")
