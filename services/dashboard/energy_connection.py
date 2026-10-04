# energy_connection.py
# Dashboard connection to the energy management system

def get_energy_data():
    """
    Get energy consumption data from the energy management system.
    This is a simple example.
    """
    return {
        "electricity_consumption_kwh": 2350,
        "electricity_tariff": 0.15,
        "status": "Acceptable"
    }

if __name__ == "__main__":
    data = get_energy_data()
    print("Energy data:", data)
