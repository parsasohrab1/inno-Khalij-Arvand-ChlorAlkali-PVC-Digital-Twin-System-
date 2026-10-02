# quality_link_model.py
# مدل پیوند کیفیت به گرید

import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# بارگذاری داده سنتتیک
df = pd.read_csv("arvand_chain_health_data_10k.csv")

# ویژگی‌ها: خلوص مواد ورودی
X = df[['vcm_purity_percent']].values
# هدف: کیفیت محصول نهایی
y = df['pvc_k_value'].values

# مدل ساده رگرسیون خطی
model = LinearRegression()
model.fit(X, y)

# ذخیره مدل
joblib.dump(model, "quality_link_model.pkl")

print("مدل پیوند کیفیت ساخته و ذخیره شد.")
