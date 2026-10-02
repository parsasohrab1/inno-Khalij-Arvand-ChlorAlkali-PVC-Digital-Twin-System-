# production_optimizer.py
# بهینه‌ساز برنامه تولید ساعتی

def optimize_production(cell_health, fouling_risk, electricity_tariff):
    """
    انتخاب بهترین ساعت برای تولید بر اساس سه ورودی:
    - سلامت سلول (۰ تا ۱۰۰، هرچه بیشتر بهتر)
    - ریسک فولینگ (۰ تا ۱۰۰، هرچه کمتر بهتر)
    - تعرفه برق (عدد، هرچه کمتر بهتر)
    """
    # امتیازدهی ساده: ترکیب وزنی
    score = (cell_health * 0.5) - (fouling_risk * 0.3) - (electricity_tariff * 0.2)
    
    if score > 50:
        return "تولید در این ساعت بهینه است."
    elif score > 20:
        return "تولید در این ساعت قابل قبول است."
    else:
        return "تولید در این ساعت توصیه نمی‌شود."

# مثال
if __name__ == "__main__":
    result = optimize_production(cell_health=85, fouling_risk=30, electricity_tariff=0.12)
    print(result)
    # نسخه اولیه بهینه‌ساز
