import requests
from weatherCLI.utils import *
from weatherCLI.config import *


class getWeather:
    def __init__(self, cityName):
        self.__BASE_URL = BASE_URL
        self.__API_KEY = API_KEY
        self.__CITY_NAME = cityName
        self.RESPONSE = {"ok"}

    def completeURL(self):
        return self.__BASE_URL + "appid=" + self.__API_KEY + "&q=" + self.__CITY_NAME

    def getResponse(self):
        return requests.get(self.completeURL()).json()

    def requiredData(self):
        response = self.getResponse()
        self.RESPONSE = {
            "currentTemp": getCurrentTemperature(response),
            "feelsLike": getFeelsLike(response),
            "windSpeed": getWindSpeed(response),
            "weatherDescription": getWeatherDescription(response),
            "sunRise": getSunRise(response),
            "sunSet": getSunSet(response),
        }
        return self.RESPONSE
