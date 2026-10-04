# tariff_connection.py
# Connection to the electricity tariff system

def get_tariff(hour):
    """
    Get the electricity tariff based on the hour.
    This is a simple example.
    """
    if 0 <= hour < 6:
        return 0.08  # off-peak tariff
    elif 6 <= hour < 18:
        return 0.15  # mid-peak tariff
    else:
        return 0.22  # peak tariff

if __name__ == "__main__":
    for h in [2, 10, 20]:
        print(f"Hour {h}: tariff = {get_tariff(h)}")
