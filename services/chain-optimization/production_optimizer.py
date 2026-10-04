# production_optimizer.py
# Hourly production schedule optimizer

def optimize_production(cell_health, fouling_risk, electricity_tariff):
    """
    Select the best hour for production based on three inputs:
    - Cell health (0 to 100, higher is better)
    - Fouling risk (0 to 100, lower is better)
    - Electricity tariff (number, lower is better)
    """
    # Simple scoring: weighted combination
    score = (cell_health * 0.5) - (fouling_risk * 0.3) - (electricity_tariff * 0.2)
    
    if score > 50:
        return "Production at this hour is optimal."
    elif score > 20:
        return "Production at this hour is acceptable."
    else:
        return "Production at this hour is not recommended."

# Example
if __name__ == "__main__":
    result = optimize_production(cell_health=85, fouling_risk=30, electricity_tariff=0.12)
    print(result)
    # Initial version of the optimizer
