from sqlalchemy import Column, Integer, String, DateTime, Enum, JSON
from app.db.base import Base
import enum
from datetime import datetime

class AlertSeverity(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"

class AlertStatus(str, enum.Enum):
    open = "open"
    acknowledged = "acknowledged"
    resolved = "resolved"

class Alert(Base):
    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    severity = Column(Enum(AlertSeverity), nullable=False, index=True)
    message = Column(String, nullable=False)
    status = Column(Enum(AlertStatus), default=AlertStatus.open, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    resolved_at = Column(DateTime, nullable=True)
    meta = Column(JSON, nullable=True)
