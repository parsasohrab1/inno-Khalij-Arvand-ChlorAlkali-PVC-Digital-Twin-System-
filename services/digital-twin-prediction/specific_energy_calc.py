# specific_energy_calc.py
# Specific energy consumption calculation

import pandas as pd

# Load data
df = pd.read_csv("arvand_chain_health_data_10k.csv")

# Specific energy consumption calculation function
def calculate_specific_energy(voltage, efficiency):
    # This is a simple sample formula.
    # In reality it must be tuned based on real data.
    constant = 1000
    return voltage * (100 / efficiency) * constant

df['calculated_energy'] = df.apply(
    lambda row: calculate_specific_energy(row['cell_voltage_v'], row['current_efficiency_percent']),
    axis=1
)

print(df[['cell_voltage_v', 'current_efficiency_percent', 'calculated_energy']].head())
print("Specific energy consumption calculation completed.")
