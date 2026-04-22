from fastapi import FastApi
class WeatherController:

    @router.post("weather/")
    def getWeather():
        return "something"