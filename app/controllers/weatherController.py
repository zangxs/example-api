from fastapi import APIRouter, Depends
from app.dto.request.weatherRequest import WeatherRequest
from app.client.weatherClient import WeatherClient
from app.repositories.weatherRepository import WeatherRepository
from app.services.weatherServices import WeatherService
from app.config.database import get_db
from sqlalchemy.orm import Session
from app.client.geocodingClient import GeoCodingClient
from app.client.weatherClient import WeatherClient
from app.client.weatherApiClient import WeatherApiClient



router = APIRouter()

def get_service() -> WeatherService:
    repository = WeatherRepository()
    geo_client = GeoCodingClient()
    weather_client = WeatherClient()
    api_client = WeatherApiClient(geo_client, weather_client)
    return WeatherService(repository, api_client)

@router.post("/weather")
def get_weather(request: WeatherRequest, db: Session = Depends(get_db), service: WeatherService = Depends(get_service)):
    return service.get_weather(db, request)