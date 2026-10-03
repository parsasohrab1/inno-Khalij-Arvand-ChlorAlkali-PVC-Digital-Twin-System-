# optimization_service.py
# سرویس بهینه‌سازی زنجیره

def optimize_production(cell_health, fouling_risk, electricity_tariff):
    """
    بهینه‌سازی برنامه تولید ساعتی بر اساس سه ورودی.
    """
    score = (cell_health * 0.5) - (fouling_risk * 0.3) - (electricity_tariff * 0.2)
    
    if score > 50:
        return {"decision": "تولید بهینه", "score": round(score, 2)}
    elif score > 20:
        return {"decision": "تولید قابل قبول", "score": round(score, 2)}
    else:
        return {"decision": "تولید توصیه نمی‌شود", "score": round(score, 2)}

if __name__ == "__main__":
    result = optimize_production(85, 30, 0.12)
    print(result)
