import argparse
from weatherCLI.weather import *

# use argparse library to create a command line tool containing name of city as an argument


def main():
    parser = argparse.ArgumentParser(description="Weather CLI Tool")
    parser.add_argument("city", metavar="CITY", type=str, help="Name of the city")
    args = parser.parse_args()

    city_name = args.city

    print(f"Fecthing the weather information for the {city_name}")

    response = getWeather(city_name).requiredData()

    # Create logical print statements based on the response dictionary and frame it as if giving a news (GPT goes Brrr....)

    print(
        f"According to the latest reports, the current temperature is {response['currentTemp']:.2f} degrees Celsius."
    )
    print(
        f"It feels like {response['feelsLike']:.2f} degrees Celsius, so be prepared for the weather conditions."
    )
    print(
        f"The wind speed is {response['windSpeed']:.2f} kilometers per hour, which may have an impact on outdoor activities."
    )

    print(
        f"In terms of the weather description, we have {response['weatherDescription']} today."
    )
    print(f"So, expect {response['weatherDescription']} throughout the day.")

    print(
        f"The sun rose at {response['sunRise']} and will set at {response['sunSet']} today."
    )
    print(
        "Make sure to plan your activities accordingly and take advantage of the daylight."
    )

    print(
        "That's all for the weather news today. Stay tuned for more updates and have a great day!"
    )


if __name__ == "__main__":
    main()
