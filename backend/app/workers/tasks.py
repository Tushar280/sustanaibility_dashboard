from celery import shared_task
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker
from app.db.session import engine
from app.services.kpi import trend_series
from app.services.anomalies import zscore_anomalies
from app.models.metrics import MetricType
from app.models.alerts import Alert, AlertSeverity

SessionLocal = sessionmaker(bind=engine)

@shared_task
def scan_anomalies():
    db = SessionLocal()
    try:
        end = datetime.utcnow()
        start = end - timedelta(days=30)
        for metric in [MetricType.energy_kwh, MetricType.water_m3, MetricType.waste_kg, MetricType.co2e_tons]:
            series = trend_series(db, metric, start, end, {})
            anomalies = zscore_anomalies(series, threshold=3.0)
            for a in anomalies:
                alert = Alert(
                    type=f"{metric.value}_anomaly",
                    severity=AlertSeverity.high,
                    message=f"Anomalous {metric.value} at {a['ts']}: {a['value']}",
                    meta={"metric": metric.value, "ts": a["ts"], "value": a["value"], "z": a["z"]}
                )
                db.add(alert)
        db.commit()
    finally:
        db.close()
