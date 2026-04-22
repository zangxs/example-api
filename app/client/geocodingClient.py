from app.dto.request.weatherRequest import WeatherRequest
import requests

class GeoCodingClient:


    def get_coordinates(self, request: WeatherRequest) -> tuple[float, float]:
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