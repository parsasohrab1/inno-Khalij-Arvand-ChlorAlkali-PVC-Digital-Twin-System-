import pandas as pd
import sqlite3

# خواندن داده سنتتیک
df = pd.read_csv("arvand_chain_health_data_10k.csv")

# اتصال به پایگاه داده
conn = sqlite3.connect("arvand_chain_health.db")

# ذخیره داده در جدول
df.to_sql("chain_health", conn, if_exists="replace", index=False)

conn.close()
print("داده با موفقیت در پایگاه داده ذخیره شد.")
