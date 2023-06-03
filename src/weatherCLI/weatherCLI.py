import argparse
from weatherCLI.weather import *

# use argparse library to create a command line tool containing name of city as an argument  

def main():
    parser = argparse.ArgumentParser(description="Weather CLI Tool")
    parser.add_argument("city",metavar="CITY",type=str,help ="Name of the city")
    args = parser.parse_args()

    city_name = args.city

    print(f"Fecthing the weather information for the {city_name}")

    response = getWeather(city_name).requiredData()

    # Create logical print statements based on the response dictionary

    print(response)


if __name__ == "__main__":
    main()
    