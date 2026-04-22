from app.dto.response.weatherResponse import WeatherResponse
from app.dto.request.weatherRequest import WeatherRequest
import requests

class WeatherClient:


    def fetch_weather(self, request: WeatherRequest, latitude: float, longitude: float) -> WeatherResponse:
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
       