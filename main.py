from fastapi import FastAPI

app = FastAPI(
    title="سامانه سلامت زنجیره اروند",
    description="سامانه پایش سلامت سلول‌های الکترولیز و پیش‌بینی فولینگ",
    version="0.1.0"
)

@app.get("/")
def read_root():
    return {"message": "سامانه سلامت زنجیره اروند فعال است."}

@app.get("/health")
def health_check():
    return {"status": "سالم"}

@app.get("/predict/membrane")
def predict_membrane(cell_voltage: float, current_efficiency: float):
    predicted = current_efficiency - 0.5
    return {
        "predicted_efficiency": predicted,
        "confidence_interval": [predicted - 0.5, predicted + 0.5]
    }

@app.get("/predict/fouling")
def predict_fouling(heat_transfer_coeff: float):
    risk = max(0, (850 - heat_transfer_coeff) / 300 * 100)
    return {"fouling_risk_percent": round(risk, 2)}

@app.get("/predict/quality")
def predict_quality(vcm_purity: float):
    k_value = 68 - 0.5 * (99.95 - vcm_purity)
    return {"predicted_k_value": round(k_value, 2)}

@app.get("/optimize")
def optimize(cell_health: float, fouling_risk: float, electricity_tariff: float):
    score = (cell_health * 0.5) - (fouling_risk * 0.3) - (electricity_tariff * 0.2)
    if score > 50:
        decision = "تولید بهینه"
    elif score > 20:
        decision = "تولید قابل قبول"
    else:
        decision = "تولید توصیه نمی‌شود"
    return {"decision": decision, "score": round(score, 2)}
