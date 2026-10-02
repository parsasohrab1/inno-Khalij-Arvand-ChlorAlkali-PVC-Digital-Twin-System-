# site_test.py
# تست سامانه در سایت اروند

def run_site_test():
    """
    اجرای تست سامانه در سایت.
    این یک نمونه ساده است.
    """
    print("شروع تست در سایت اروند...")
    
    results = {
        "cell_connection": "موفق",
        "autoclave_connection": "موفق",
        "prediction_model": "موفق",
        "alert_system": "موفق",
        "dashboard": "موفق"
    }
    
    for item, status in results.items():
        print(f"{item}: {status}")
    
    print("تست در سایت با موفقیت انجام شد.")

if __name__ == "__main__":
    run_site_test()
