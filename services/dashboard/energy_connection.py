# energy_connection.py
# اتصال داشبورد به سامانه مدیریت انرژی

def get_energy_data():
    """
    دریافت داده مصرف انرژی از سامانه مدیریت انرژی.
    این یک نمونه ساده است.
    """
    return {
        "electricity_consumption_kwh": 2350,
        "electricity_tariff": 0.15,
        "status": "قابل قبول"
    }

if __name__ == "__main__":
    data = get_energy_data()
    print("داده انرژی:", data)
