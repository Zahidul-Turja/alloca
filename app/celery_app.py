import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

celery_app = Celery(
        "alloc",
        broker=os.getenv("REDIS_URL"),
        backend=os.getenv("REDIS_URL"),
        include=["app.tasks"],
    )

celery_app.conf.timezone = "UTC"
