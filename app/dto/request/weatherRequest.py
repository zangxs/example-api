from pydantic import BaseModel, field_validator
from datetime import date
from typing import Optional

class WeatherRequest(BaseModel):
    ciudad: str
    date: Optional[date] = None

    @field_validator("date")
    @classmethod
    def date_not_older_than_10_days(cls, v):
        if v is None:
            return v
        if v < date.today() - timedelta(days=10):
            raise ValueError("La fecha no puede ser mayor a 10 días atrás")
        return v