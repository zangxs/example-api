from fastapi import APIRouter
from app.dto.request.weatherRequest import WeatherRequest

router = APIRouter()

@router.post("/weather")
def get_weather(request: WeatherRequest):
    return {"ciudad": "mi ciudad es " + request.ciudad}