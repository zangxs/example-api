from fastapi import APIRouter
from app.dto.request.weatherRequest import WeatherRequest

router = APIRouter()

@router.post("/weather")
def get_weather(request: WeatherRequest):  # FastAPI lee el type hint y sabe que es body
    return {"ciudad": "mi ciudad es " + request.ciudad}