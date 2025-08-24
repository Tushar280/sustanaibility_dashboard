from fastapi import APIRouter
from app.db.session import SessionLocal
from app.models.alerts import Alert
router = APIRouter(prefix="/alerts", tags=["alerts"])

@router.get("/list")
def list_alerts():
    db = SessionLocal()
    try:
        rows = db.query(Alert).order_by(Alert.created_at.desc()).limit(100).all()
        return [{
            "id": r.id,
            "type": r.type,
            "severity": r.severity.value,
            "message": r.message,
            "status": r.status.value,
            "created_at": r.created_at.isoformat(),
            "resolved_at": r.resolved_at.isoformat() if r.resolved_at else None,
            "meta": r.meta
        } for r in rows]
    finally:
        db.close()
