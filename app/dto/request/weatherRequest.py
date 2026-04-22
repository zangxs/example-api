from pydantic import BaseModel, field_validator
from datetime import date as date_type, timedelta
from typing import Optional

class WeatherRequest(BaseModel):
    ciudad: str
    pais: str
    date: Optional[date_type] = None

    @field_validator("date", mode="before")
    @classmethod
    def date_not_older_than_10_days(cls, v):
        if v is None:
            return date_type.today()
        v = date_type.fromisoformat(str(v))
        if v < date_type.today() - timedelta(days=10):
            raise ValueError("La fecha no puede ser mayor a 10 días atrás")
        return v