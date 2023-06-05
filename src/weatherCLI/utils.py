# Helper function to format the output to a human readable format.
import pytz  # timezone function
import datetime as dt

# write a function to convert temperature in kelvin to celsius
def kelvinToCelsius(temp):
    celsius = temp - 273.15
    return celsius


# write a function to convert timestamp to GMT+5:30 time
def convert_to_gmt_plus_5_30(timestamp):
    # Create a timezone object for GMT +5:30
    gmt_plus_5_30 = pytz.timezone("Asia/Kolkata")

    # Convert the timestamp to datetime object in UTC
    utc_time = dt.datetime.utcfromtimestamp(timestamp)

    # Convert the UTC time to GMT +5:30 time
    gmt_plus_5_30_time = utc_time.replace(tzinfo=pytz.utc).astimezone(gmt_plus_5_30)

    return gmt_plus_5_30_time


# write function getCurrentTemperature that takes input as response and
# uses kelvinToCelsius to return the output of response['main']['temp']
def getCurrentTemperature(response):
    temp = response["main"]["temp"]
    return kelvinToCelsius(temp)


# write function getFeelsLike that takes input as response and
# uses kelvinToCelsius to return the output of response['main']['feels_like']
def getFeelsLike(response):
    temp = response["main"]["feels_like"]
    return kelvinToCelsius(temp)


# write function getWindSpeed that takes input as response
# return the output of response['wind']['speed']
def getWindSpeed(response):
    # modify this function based on the response
    return response["wind"]["speed"]


# write function getWeatherDescription that takes input as response
# return the output of response['weather'][0]['description']
def getWeatherDescription(response):
    # modify this function based on the response
    return response["weather"][0]["description"]


# write function getSunRise that takes input as response and
# uses convert_to_gmt_plus_5_30 to return the string output of reponse['sys']['sunrise']
def getSunRise(response):
    # modify this function based on the response
    return str(convert_to_gmt_plus_5_30(response["sys"]["sunrise"]))


# write function getSunSet that takes input as response and
# uses convert_to_gmt_plus_5_30 to return the string output of rreponse['sys']['sunset']
def getSunSet(reponse):
    # modify this function based on the response
    return str(convert_to_gmt_plus_5_30(reponse["sys"]["sunset"]))
