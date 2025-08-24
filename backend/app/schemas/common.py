from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Filters(BaseModel):
    start: datetime
    end: datetime
    unit_id: Optional[int] = None
    department_id: Optional[int] = None
    machine_id: Optional[int] = None
    shift_id: Optional[int] = None
