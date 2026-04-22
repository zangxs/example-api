from app.dto.response.weatherResponse import WeatherResponse
from app.dto.request.weatherRequest import WeatherRequest
from app.client.geocodingClient import GeoCodingClient
from app.client.weatherClient import WeatherClient

class WeatherApiClient:
        
    def __init__(self, geoCodingClient: GeoCodingClient, weatherClient: WeatherClient):
        self.geoCodingClient = geoCodingClient
        self.weatherClient = weatherClient

    def search_weather_by_city_and_date(self, request: WeatherRequest) -> WeatherResponse:
        latitude, longitude = self.geoCodingClient.get_coordinates(request)
        return self.weatherClient.fetch_weather(request, latitude, longitude)