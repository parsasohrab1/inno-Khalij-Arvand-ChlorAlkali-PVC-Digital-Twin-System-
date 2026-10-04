import numpy as np
import pandas as pd
from datetime import datetime, timedelta

NUM_RECORDS = 10000
START_TIME = datetime(2026, 9, 14, 8, 0, 0)
timestamps = [START_TIME + timedelta(seconds=i) for i in range(NUM_RECORDS)]
t = np.linspace(0, 20 * np.pi, NUM_RECORDS)

# 1. Membrane electrolysis cell
cell_voltage_v = 3.05 + 0.00004 * np.arange(NUM_RECORDS) + 0.02 * np.sin(t * 0.3) + np.random.normal(0, 0.01, NUM_RECORDS)
current_efficiency_percent = 96.5 - 0.0003 * np.arange(NUM_RECORDS) + np.random.normal(0, 0.3, NUM_RECORDS)
current_efficiency_percent = np.clip(current_efficiency_percent, 88, 97)
specific_energy_kwh_per_ton = 2350 + 15 * (cell_voltage_v - 3.05) * 100 + np.random.normal(0, 20, NUM_RECORDS)

# 2. PVC polymerization autoclave
jacket_heat_transfer_coeff = 850 - 0.03 * np.arange(NUM_RECORDS) + np.random.normal(0, 15, NUM_RECORDS)
jacket_heat_transfer_coeff = np.clip(jacket_heat_transfer_coeff, 400, 900)
agitator_motor_power_kw = 120 + 0.002 * np.arange(NUM_RECORDS) + np.random.normal(0, 3, NUM_RECORDS)
batch_cycle_time_min = 240 + 0.004 * np.arange(NUM_RECORDS) + np.random.normal(0, 5, NUM_RECORDS)

# 3. Product quality
vcm_purity_percent = 99.9 - 0.02 * (100 - current_efficiency_percent) / 8 + np.random.normal(0, 0.02, NUM_RECORDS)
pvc_k_value = 68 - 0.5 * (99.95 - vcm_purity_percent) + np.random.normal(0, 0.3, NUM_RECORDS)

# 4. Labels
needs_wash_7d = (jacket_heat_transfer_coeff < 550).astype(int)
membrane_replace_flag_90d = (current_efficiency_percent < 90).astype(int)

df = pd.DataFrame({
    'timestamp': timestamps,
    'cell_voltage_v': np.round(cell_voltage_v, 4),
    'current_efficiency_percent': np.round(current_efficiency_percent, 2),
    'specific_energy_kwh_per_ton': np.round(specific_energy_kwh_per_ton, 1),
    'jacket_heat_transfer_coeff': np.round(jacket_heat_transfer_coeff, 1),
    'agitator_motor_power_kw': np.round(agitator_motor_power_kw, 2),
    'batch_cycle_time_min': np.round(batch_cycle_time_min, 1),
    'vcm_purity_percent': np.round(vcm_purity_percent, 3),
    'pvc_k_value': np.round(pvc_k_value, 2),
    'needs_wash_7d': needs_wash_7d,
    'membrane_replace_flag_90d': membrane_replace_flag_90d,
})

df.to_csv("arvand_chain_health_data_10k.csv", index=False)
print(f"✅ Saved. Records: {len(df):,} - Variables: {len(df.columns)}")
print(df.describe())
