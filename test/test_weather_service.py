from unittest.mock import MagicMock
from app.services.weatherServices import WeatherService
from app.dto.request.weatherRequest import WeatherRequest
from app.dto.response.weatherResponse import WeatherResponse
from datetime import date

def test_get_weather_returns_from_db_when_exists():
    # equivalente a @Mock
    mock_repository = MagicMock()
    mock_client = MagicMock()

    # equivalente a @InjectMocks
    service = WeatherService(mock_repository, mock_client)

    # datos de prueba
    request = WeatherRequest(ciudad="Cucuta", pais="Colombia", date=date.today())
    expected = WeatherResponse(ciudad="Cucuta", pais="Colombia", date=date.today(), temp_cent=30.0, temp_far=86.0)

    # equivalente a when(repository.search).thenReturn(expected)
    mock_repository.search_by_city_and_date.return_value = expected

    # ejecutar
    result = service.get_weather(MagicMock(), request)

    # verificar que retornó lo de DB
    assert result == expected

    # equivalente a verify(client, never()).search()
    mock_client.search_weather_by_city_and_date.assert_not_called()


def test_get_weather_calls_api_when_not_in_db():
    mock_repository = MagicMock()
    mock_client = MagicMock()
    service = WeatherService(mock_repository, mock_client)

    request = WeatherRequest(ciudad="Cucuta", pais="Colombia", date=date.today())
    api_response = WeatherResponse(ciudad="Cucuta", pais="Colombia", date=date.today(), temp_cent=30.0, temp_far=86.0)

    # simula que no existe en DB
    mock_repository.search_by_city_and_date.return_value = None
    mock_client.search_weather_by_city_and_date.return_value = api_response

    result = service.get_weather(MagicMock(), request)

    # verificó en DB
    mock_repository.search_by_city_and_date.assert_called_once()
    # llamó al client
    mock_client.search_weather_by_city_and_date.assert_called_once()
    # guardó en DB
    mock_repository.save.assert_called_once()