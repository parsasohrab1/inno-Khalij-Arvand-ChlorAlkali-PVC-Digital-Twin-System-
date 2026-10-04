# wash_alert.py
# Washing alert system

def check_wash_alert(heat_transfer_coeff, motor_power):
    if heat_transfer_coeff < 550:
        return "Alert: immediate washing required"
    elif heat_transfer_coeff < 650:
        return "Alert: about 5 days until washing"
    else:
        return "Normal status"

print(check_wash_alert(500, 125))
