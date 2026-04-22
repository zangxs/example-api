from unittest.mock import MagicMock, patch
from app.dto.request.weatherRequest import WeatherRequest
from app.dto.response.weatherResponse import WeatherResponse
from app.client.weatherClient import WeatherClient
from datetime import date



def test_fetch_weather_calls_correct_url():
    client = WeatherClient()
    request = WeatherRequest(ciudad="cucuta", pais="colombia", date=date.today())
    latitude =  7.89
    longitude = -72.50

    # simulamos la respuesta del API externo
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "latitude": 7.89,
        "longitude": -72.50,
        "generationtime_ms": 2.2119,
        "utc_offset_seconds": 0,
        "timezone": "Europe/Berlin",
        "timezone_abbreviation": "CEST",
        "daily": {
            "temperature_2m_max": [13, 12.7, 12.7, 12.5, 12.5, 12.8, 13, 12.9, 13.3, ...]
        }
    }
    with patch("app.client.weatherClient.requests.get", return_value=mock_response):
        result = client.fetch_weather(request, latitude, longitude)

    assert result == WeatherResponse(ciudad='cucuta', pais='colombia', date=date.today(), temp_cent=13.0, temp_far=55.4)
    
    

    