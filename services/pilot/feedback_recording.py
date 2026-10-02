# feedback_recording.py
# ثبت بازخورد واقعی برای بازآموزی مدل

def record_feedback(feedback_type, value, note=""):
    """
    ثبت بازخورد واقعی.
    
    ورودی:
        feedback_type: نوع بازخورد (تعویض غشا یا شست‌وشو)
        value: مقدار واقعی ثبت‌شده
        note: توضیح اضافی
    """
    feedback = {
        "type": feedback_type,
        "value": value,
        "note": note
    }
    print("بازخورد ثبت شد:", feedback)
    return feedback

if __name__ == "__main__":
    record_feedback("تعویض غشا", "1405-07-15", "غشای سلول ۳ تعویض شد.")
    record_feedback("شست‌وشو", "1405-07-20", "اتوکلاو ۲ شست‌وشو شد.")
