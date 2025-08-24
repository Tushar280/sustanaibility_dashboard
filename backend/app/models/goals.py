from sqlalchemy import Column, Integer, Float, Date, Enum, ForeignKey
from app.db.base import Base
from app.models.metrics import MetricType

class Goal(Base):
    __tablename__ = "goals"
    id = Column(Integer, primary_key=True)
    metric_type = Column(Enum(MetricType), nullable=False, index=True)
    target_value = Column(Float, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    unit_id = Column(Integer, ForeignKey("units.id"), nullable=True)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=True)
