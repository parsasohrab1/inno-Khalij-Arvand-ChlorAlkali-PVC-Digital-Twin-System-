# tariff_connection.py
# اتصال به سامانه تعرفه برق

def get_tariff(hour):
    """
    دریافت تعرفه برق بر اساس ساعت.
    این یک نمونه ساده است.
    """
    if 0 <= hour < 6:
        return 0.08  # تعرفه کم‌باری
    elif 6 <= hour < 18:
        return 0.15  # تعرفه میان‌باری
    else:
        return 0.22  # تعرفه اوج‌باری

if __name__ == "__main__":
    for h in [2, 10, 20]:
        print(f"ساعت {h}: تعرفه = {get_tariff(h)}")
