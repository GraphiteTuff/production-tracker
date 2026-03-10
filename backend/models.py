from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime


class ProductionRecord(BaseModel):
    part_id: str
    status: str
    quality_metrics: Dict
    batch_id: Optional[str] = None
    production_timestamp: Optional[datetime] = None