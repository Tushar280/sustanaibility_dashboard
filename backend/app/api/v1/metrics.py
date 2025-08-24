from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime
from app.db.session import SessionLocal
from app.models.metrics import MetricFact, MetricType

router = APIRouter(prefix="/metrics", tags=["metrics"])

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.get("/hotspots")
def hotspots(metric: MetricType, start: datetime, end: datetime, by: str = "department", db: Session = Depends(get_db)):
    col = {
        "unit": MetricFact.unit_id,
        "department": MetricFact.department_id,
        "machine": MetricFact.machine_id,
        "shift": MetricFact.shift_id,
    }[by]
    q = db.query(col.label("key"), func.sum(MetricFact.value).label("value")).filter(
        MetricFact.metric_type == metric,
        MetricFact.ts >= start,
        MetricFact.ts <= end
    ).group_by(col).order_by(func.sum(MetricFact.value).desc()).limit(10)
    return [{"key": r.key, "value": float(r.value)} for r in q.all()]
