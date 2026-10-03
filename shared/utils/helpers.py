# helpers.py
# ابزارهای کمکی مشترک

def format_number(value, decimals=2):
    """قالب‌بندی عدد با تعداد اعشار مشخص."""
    return round(value, decimals)

def calculate_efficiency(voltage, current):
    """محاسبه راندمان ساده."""
    if current == 0:
        return 0
    return (voltage * current) / 100
