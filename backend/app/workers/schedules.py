from app.workers.celery_app import celery
celery.conf.beat_schedule = {
    "scan-anomalies-15min": {"task": "app.workers.tasks.scan_anomalies", "schedule": 900.0}
}
