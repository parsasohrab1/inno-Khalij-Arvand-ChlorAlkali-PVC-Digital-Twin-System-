# specific_energy_calc.py
# محاسبه مصرف انرژی ویژه

import pandas as pd

# بارگذاری داده
df = pd.read_csv("arvand_chain_health_data_10k.csv")

# تابع محاسبه مصرف انرژی ویژه
def calculate_specific_energy(voltage, efficiency):
    # این یک فرمول ساده و نمونه است.
    # در واقعیت باید بر اساس داده‌های واقعی تنظیم شود.
    constant = 1000
    return voltage * (100 / efficiency) * constant

df['calculated_energy'] = df.apply(
    lambda row: calculate_specific_energy(row['cell_voltage_v'], row['current_efficiency_percent']),
    axis=1
)

print(df[['cell_voltage_v', 'current_efficiency_percent', 'calculated_energy']].head())
print("محاسبه مصرف انرژی ویژه انجام شد.")
