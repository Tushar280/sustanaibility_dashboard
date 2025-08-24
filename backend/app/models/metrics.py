from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, Float, Index
from sqlalchemy.orm import relationship
from app.db.base import Base
import enum

class MetricType(str, enum.Enum):
    energy_kwh = "energy_kwh"
    water_m3 = "water_m3"
    waste_kg = "waste_kg"
    co2e_tons = "co2e_tons"

class MetricFact(Base):
    __tablename__ = "metric_facts"
    id = Column(Integer, primary_key=True)
    ts = Column(DateTime, index=True, nullable=False)
    unit_id = Column(Integer, ForeignKey("units.id"), nullable=True, index=True)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=True, index=True)
    machine_id = Column(Integer, ForeignKey("machines.id"), nullable=True, index=True)
    shift_id = Column(Integer, ForeignKey("shifts.id"), nullable=True, index=True)
    metric_type = Column(Enum(MetricType), index=True, nullable=False)
    value = Column(Float, nullable=False)
    __table_args__ = (
        Index("ix_metric_dim_ts", "ts", "metric_type", "unit_id", "department_id", "machine_id", "shift_id"),
    )
