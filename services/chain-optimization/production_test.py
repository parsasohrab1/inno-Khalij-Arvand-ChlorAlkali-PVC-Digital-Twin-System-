# production_test.py
# تست برنامه تولید بهینه

from production_optimizer import optimize_production
from tariff_connection import get_tariff

def run_test():
    # داده نمونه
    cell_health = 85
    fouling_risk = 30

    for hour in [2, 10, 20]:
        tariff = get_tariff(hour)
        result = optimize_production(cell_health, fouling_risk, tariff)
        print(f"ساعت {hour} | تعرفه {tariff} | نتیجه: {result}")

if __name__ == "__main__":
    run_test()
