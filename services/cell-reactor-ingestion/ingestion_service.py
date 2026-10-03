# ingestion_service.py
# سرویس دریافت داده سلول و راکتور

import pandas as pd

def load_synthetic_data(file_path="arvand_chain_health_data_10k.csv"):
    """
    بارگذاری داده سنتتیک.
    بعداً با داده واقعی از سیستم کنترل جایگزین می‌شود.
    """
    df = pd.read_csv(file_path)
    return df

def ingest_data(df):
    """
    ارسال داده به پایگاه داده.
    این یک نمونه ساده است.
    """
    print(f"تعداد رکوردهای دریافتی: {len(df)}")
    print("داده با موفقیت دریافت شد.")
    return True

if __name__ == "__main__":
    data = load_synthetic_data()
    ingest_data(data)
