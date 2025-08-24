from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from datetime import datetime
from app.db.session import SessionLocal
from app.services.kpi import sum_metric, trend_series
from app.models.metrics import MetricType

router = APIRouter(prefix="/kpis", tags=["kpis"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/overview")
def overview(
    start: datetime = Query(...),
    end: datetime = Query(...),
    unit_id: int | None = None,
    department_id: int | None = None,
    machine_id: int | None = None,
    shift_id: int | None = None,
    db: Session = Depends(get_db)
):
    filters = dict(unit_id=unit_id, department_id=department_id, machine_id=machine_id, shift_id=shift_id)
    metrics = [MetricType.energy_kwh, MetricType.water_m3, MetricType.waste_kg, MetricType.co2e_tons]
    data = {}
    for m in metrics:
        value = sum_metric(db, m, start, end, filters)
        series = trend_series(db, m, start, end, filters)
        data[m.value] = {"value": value, "series": series}
    return {"kpis": data}
