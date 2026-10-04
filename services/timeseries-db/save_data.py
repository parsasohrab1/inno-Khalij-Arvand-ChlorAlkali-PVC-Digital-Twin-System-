import pandas as pd
import sqlite3

# Read the synthetic data
df = pd.read_csv("arvand_chain_health_data_10k.csv")

# Connect to the database
conn = sqlite3.connect("arvand_chain_health.db")

# Save the data to a table
df.to_sql("chain_health", conn, if_exists="replace", index=False)

conn.close()
print("Data saved successfully to the database.")
