# alert_system.py
# Real-time alert system

def check_alerts(cell_health, fouling_risk):
    """
    Check the status and generate the appropriate alert.
    """
    alerts = []
    
    if cell_health < 90:
        alerts.append("Alert: cell health is low.")
    
    if fouling_risk > 70:
        alerts.append("Alert: fouling risk is high.")
    
    if not alerts:
        return "Normal status."
    
    return " | ".join(alerts)

if __name__ == "__main__":
    print(check_alerts(85, 75))
