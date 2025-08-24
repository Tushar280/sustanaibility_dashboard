from sqlalchemy.orm import Session
from datetime import datetime
from app.models.metrics import MetricFact, MetricType
from sqlalchemy import func

def apply_filters(q, filters: dict):
    mapping = [
        ("unit_id", MetricFact.unit_id),
        ("department_id", MetricFact.department_id),
        ("machine_id", MetricFact.machine_id),
        ("shift_id", MetricFact.shift_id),
    ]
    for key, col in mapping:
        v = filters.get(key)
        if v:
            q = q.filter(col == v)
    return q

def sum_metric(db: Session, metric: MetricType, start: datetime, end: datetime, filters: dict):
    q = db.query(func.sum(MetricFact.value)).filter(
        MetricFact.metric_type == metric,
        MetricFact.ts >= start,
        MetricFact.ts <= end,
    )
    q = apply_filters(q, filters)
    return float(q.scalar() or 0.0)

def trend_series(db: Session, metric: MetricType, start: datetime, end: datetime, filters: dict, interval="day"):
    trunc = func.date_trunc(interval, MetricFact.ts).label("bucket")
    q = db.query(trunc, func.sum(MetricFact.value).label("value")).filter(
        MetricFact.metric_type == metric,
        MetricFact.ts >= start,
        MetricFact.ts <= end,
    )
    q = apply_filters(q, filters)
    q = q.group_by(trunc).order_by(trunc.asc())
    return [{"ts": r.bucket.isoformat(), "value": float(r.value)} for r in q.all()]
