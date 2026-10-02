# wash_time_calc.py
# محاسبه زمان بهینه شست‌وشو

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# بارگذاری داده سنتتیک
df = pd.read_csv("arvand_chain_health_data_10k.csv")

# ویژگی‌ها: ضریب انتقال حرارت و توان همزن
X = df[['jacket_heat_transfer_coeff', 'agitator_motor_power_kw']].values
# هدف: زمان سیکل (به عنوان معیار نیاز به شست‌وشو)
y = df['batch_cycle_time_min'].values

# مدل ساده رگرسیون خطی
model = LinearRegression()
model.fit(X, y)

# ذخیره مدل
joblib.dump(model, "wash_time_model.pkl")

# محاسبه زمان تقریبی تا شست‌وشو
def estimate_wash_time(heat_transfer_coeff, motor_power):
    # اگر ضریب انتقال حرارت کم شود، زمان شست‌وشو نزدیک است
    if heat_transfer_coeff < 550:
        return "نیاز فوری به شست‌وشو"
    elif heat_transfer_coeff < 650:
        return "حدود ۵ روز تا شست‌وشو"
    else:
        return "وضعیت عادی"

print(estimate_wash_time(500, 125))
print("محاسبه زمان شست‌وشو انجام شد.")
