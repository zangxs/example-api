from app.dto.response.weatherResponse import WeatherResponse
from app.dto.request.weatherRequest import WeatherRequest
import requests

class WeatherClient:

    def _get_coordinates(self, request: WeatherRequest) -> tuple[float, float]:
        url = "https://geocoding-api.open-meteo.com/v1/search?name=" + request.ciudad
        response = requests.get(url)
        response.raise_for_status()

        results = response.json().get("results", [])
        location = next(
            (r for r in results if r["country"].lower() == request.pais.lower()),
            None
        )

        if location is None:
            raise ValueError(f"No se encontró {request.ciudad} en {request.pais}")

        return location["latitude"], location["longitude"]
    
    def _fetch_weather(self, request: WeatherRequest, latitude: float, longitude: float) -> WeatherResponse:
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "daily": "temperature_2m_max,temperature_2m_min",
            "start_date": str(request.date),
            "end_date": str(request.date)
        }

        response = requests.get("https://api.open-meteo.com/v1/forecast", params=params)
        response.raise_for_status()

        data = response.json()
        temp_cent = data["daily"]["temperature_2m_max"][0]
        temp_far = round((temp_cent * 9/5) + 32, 2)

        return WeatherResponse(
            ciudad=request.ciudad,
            pais=request.pais,
            date=request.date,
            temp_cent=temp_cent,
            temp_far=temp_far
        )

    def search_weather_by_city_and_date(self, request: WeatherRequest) -> WeatherResponse:
        latitude, longitude = self._get_coordinates(request)
        return self._fetch_weather(request, latitude, longitude)
       