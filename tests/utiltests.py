import unittest
from unittest.mock import MagicMock
from weatherCLI.utils import (
    kelvinToCelsius,
    convert_to_gmt_plus_5_30,
    getCurrentTemperature,
    getFeelsLike,
    getWindSpeed,
    getWeatherDescription,
    getSunRise,
    getSunSet,
)

class WeatherModuleTests(unittest.TestCase):
    def test_kelvin_to_celsius(self):
        celsius = kelvinToCelsius(300)
        self.assertAlmostEqual(celsius, 26.85, places=2)

    def test_convert_to_gmt_plus_5_30(self):
        timestamp = 1622745600  # Assuming timestamp in UTC
        converted_time = convert_to_gmt_plus_5_30(timestamp)
        # Modify this assertion based on the expected converted time
        self.assertEqual(str(converted_time), "2021-06-04 00:10:00+05:30")

    def test_get_current_temperature(self):
        response = {"main": {"temp": 293.15}}
        temperature = getCurrentTemperature(response)
        self.assertAlmostEqual(temperature, 20.0, places=2)

    def test_get_feels_like(self):
        response = {"main": {"feels_like": 295.0}}
        feels_like = getFeelsLike(response)
        self.assertAlmostEqual(feels_like, 21.85, places=2)

    def test_get_wind_speed(self):
        response = {"wind": {"speed": 3.5}}
        wind_speed = getWindSpeed(response)
        self.assertEqual(wind_speed, 3.5)

    def test_get_weather_description(self):
        response = {"weather": [{"description": "Cloudy"}]}
        description = getWeatherDescription(response)
        self.assertEqual(description, "Cloudy")

    def test_get_sun_rise(self):
        response = {"sys": {"sunrise": 1622714760}}  # Assuming timestamp in UTC
        sun_rise = getSunRise(response)
        # Modify this assertion based on the expected converted time
        self.assertEqual(str(sun_rise), "2021-06-03 15:36:00+05:30")

    def test_get_sun_set(self):
        response = {"sys": {"sunset": 1622771460}}  # Assuming timestamp in UTC
        sun_set = getSunSet(response)
        # Modify this assertion based on the expected converted time
        self.assertEqual(str(sun_set), "2021-06-04 07:21:00+05:30")


if __name__ == "__main__":
    unittest.main()
