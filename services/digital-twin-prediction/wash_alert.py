# wash_alert.py
# سامانه هشدار شست‌وشو

def check_wash_alert(heat_transfer_coeff, motor_power):
    if heat_transfer_coeff < 550:
        return "هشدار: نیاز فوری به شست‌وشو"
    elif heat_transfer_coeff < 650:
        return "هشدار: حدود ۵ روز تا شست‌وشو"
    else:
        return "وضعیت عادی"

print(check_wash_alert(500, 125))
