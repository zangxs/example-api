from app.repositories.weatherRepository import WeatherRepository
from app.client.weatherClient import WeatherClient
from app.dto.request.weatherRequest import WeatherRequest
from app.dto.response.weatherResponse import WeatherResponse
from app.entities.weatherEntity import WeatherEntity
from sqlalchemy.orm import Session
from datetime import date 

class WeatherService:

    def __init__(self, repository: WeatherRepository, client: WeatherClient):
        self.repository = repository
        self.client = client

    def get_weather(self, db: Session, request: WeatherRequest)-> WeatherResponse:
        #Validacion de la fecha
        if request.date is None:
            request.date = date.today()

        #primero busca en db
        weather_entity = self.repository.search_by_city_and_date(db, request)

        if weather_entity is not None:
            return weather_entity

        #si no existe llama al api
        weather_data = self.client.search_weather_by_city_and_date(request)

        #crear el entity y guardar
        entity_to_save = WeatherEntity()
        entity_to_save.ciudad = weather_data.ciudad
        entity_to_save.date = weather_data.date
        entity_to_save.pais = weather_data.pais
        entity_to_save.temp_cent = weather_data.temp_cent
        entity_to_save.temp_far = weather_data.temp_far

        return self.repository.save(db, entity_to_save)