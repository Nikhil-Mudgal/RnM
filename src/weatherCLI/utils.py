# Helper function to format the output to a human readable format.
def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

def getCurrentTemperature(response):
    # modify this function based on the response
    temp_kelvin = response['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)

def getFeelsLike(response):
    # modify this function based on the response
    feels_like_kelvin = response['main']['feels_like']
    feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)

def getWindSpeed(response):
    # modify this function based on the response
    wind_speed = response['main']['humidity']

def getWeatherDescription(response):
    # modify this function based on the response
    description = response['weather'][0]['description']

def getSunRise(response):
    # modify this function based on the response
    sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])

def getSunSet(reponse):
    # modify this function based on the response
    sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
