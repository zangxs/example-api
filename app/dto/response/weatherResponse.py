from pydantic import BaseModel
from datetime import date as date_type

class WeatherResponse(BaseModel):
    ciudad: str
    pais: str
    date: date_type
    temp_cent: float
    temp_far: float
