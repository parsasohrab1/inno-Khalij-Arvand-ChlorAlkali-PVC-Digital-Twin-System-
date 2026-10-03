# settings.py
# تنظیمات پروژه

import os
from dotenv import load_dotenv

load_dotenv()

# تنظیمات پایگاه داده
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./arvand_chain_health.db")

# تنظیمات صف پیام
MESSAGE_QUEUE_HOST = os.getenv("MESSAGE_QUEUE_HOST", "localhost")
MESSAGE_QUEUE_PORT = int(os.getenv("MESSAGE_QUEUE_PORT", 9092))

# تنظیمات مدل‌ها
MODEL_PATH = os.getenv("MODEL_PATH", "./models/")
