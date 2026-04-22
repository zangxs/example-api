from fastapi import APIRouter
from schemas import WeatherRequest

router = APIRouter()

@router.post("/weather")
def get_weather(request: WeatherRequest):  # FastAPI lee el type hint y sabe que es body
    return {"ciudad": request.ciudad}