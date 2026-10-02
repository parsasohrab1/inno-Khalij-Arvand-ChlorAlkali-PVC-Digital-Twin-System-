# alert_system.py
# سامانه هشدار بلادرنگ

def check_alerts(cell_health, fouling_risk):
    """
    بررسی وضعیت و تولید هشدار مناسب.
    """
    alerts = []
    
    if cell_health < 90:
        alerts.append("هشدار: سلامت سلول پایین است.")
    
    if fouling_risk > 70:
        alerts.append("هشدار: ریسک فولینگ بالا است.")
    
    if not alerts:
        return "وضعیت عادی."
    
    return " | ".join(alerts)

if __name__ == "__main__":
    print(check_alerts(85, 75))
