from sqlalchemy.orm import Session
from app.models.goals import Goal
from app.models.metrics import MetricType, MetricFact
from sqlalchemy import func

def goal_status(db: Session, metric: MetricType, start, end, filters: dict):
    g = db.query(Goal).filter(
        Goal.metric_type == metric,
        Goal.start_date <= end.date(),
        Goal.end_date >= start.date()
    ).first()
    target = g.target_value if g else None
    actual = db.query(func.sum(MetricFact.value)).filter(
        MetricFact.metric_type == metric,
        MetricFact.ts >= start,
        MetricFact.ts <= end
    ).scalar() or 0.0
    progress = None
    if target:
        progress = float(actual) / float(target) if target != 0 else None
    return {"target": target, "actual": float(actual), "progress": progress}
