import datetime
from typing import Optional
from pydantic import BaseModel
from models.location import Location


class ReportSubmital(BaseModel):
    description: str
    location: Location


class Report(ReportSubmital):
    id: str
    created_date: Optional[datetime.datetime]
