import requests
from utils import *

class getWeather:
    def __init__(self,cityName):
        self.__BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        self.__API_KEY = open('src/api_key','r').read()
        self.__CITY_NAME = cityName
        self.RESPONSE = {"ok"}

    def completeURL(self):
        return self.__BASE_URL + "appid=" + self.__API_KEY + "&q=" + self.__CITY_NAME

    def getResponse(self):
        return requests.get(self.completeURL()).json()

    def requiredData(self):
        response = self.getResponse()
        self.RESPONSE = {
            "currentTemp" : getCurrentTemperature(response),
            "feelsLike" : getFeelsLike(response),
            "windSpeed" : getWindSpeed(response),
            "weatherDescription" : getWeatherDescription(response),
            "sunRise" : getSunRise(response),
            "sunSet" : getSunSet(response)
        }
        return self.RESPONSE

response = getWeather("Paris").requiredData()

print(response)