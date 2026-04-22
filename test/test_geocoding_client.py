from app.dto.request.weatherRequest import WeatherRequest
from app.client.weatherApiClient import GeoCodingClient
from unittest.mock import MagicMock, patch
from datetime import date
import pytest


def test_get_coordinates_calls_correct_url():
    client = GeoCodingClient()

    # datos de prueba
    request = WeatherRequest(ciudad="Cucuta", pais="Colombia", date=date.today())

    # simulamos la respuesta del API externo
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "results": [
            {"country": "Colombia", "latitude": 7.89, "longitude": -72.50},
            {"country": "Venezuela", "latitude": 10.15, "longitude": -64.28}
        ]
    }

    with patch("app.client.geocodingClient.requests.get", return_value=mock_response):
        result = client.get_coordinates(request)

    assert result == (7.89, -72.50)

def test_no_results():
    client = GeoCodingClient()
    request = WeatherRequest(ciudad="Cucuta", pais="Japon", date=date.today())

    mock_response = MagicMock()
    mock_response.json.return_value = {
        "results": [
            {"country": "Colombia", "latitude": 7.89, "longitude": -72.50}
        ]
    }

    with patch("app.client.geocodingClient.requests.get", return_value=mock_response):
        try:
            client.get_coordinates(request)
            assert False, "Debió lanzar ValueError"
        except ValueError as e:
            assert "Japon" in str(e)
