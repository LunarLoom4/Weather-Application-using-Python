# Importing the load_dotenv function to load environment variables from a .env file
from dotenv import load_dotenv

# Importing pprint to nicely format (pretty print) the output data
from pprint import pprint

# Importing requests to allow Python to make HTTP requests to web APIs
import requests

# Importing os to access environment variables like the API key
import os

# Load environment variables from a .env file (e.g., API_KEY)
load_dotenv()

# Define a function to get the current weather data for a given city
def get_current_weather(city='Hadapsar'):
    # Construct the URL for the weather API request using the API key and city
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    # Send a GET request to the API and get the response in JSON format
    weather_data = requests.get(request_url).json()

    # Return the weather data dictionary
    return weather_data

# This block only runs if this script is executed directly (not when imported as a module)
if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')

    # Ask the user to enter a city name
    city = input("Please enter a city name: ")

    # Check for empty strings or string with only spaces
    if not bool(city.strip()):
        city = 'Hadapsar'
    else:
        city = city.strip()

    # Call the function to get weather data for the entered city
    weather_data = get_current_weather(city)

    # Print the weather data in a readable format
    print()
    pprint(weather_data)  # Pretty-print the JSON response
    print()

    if weather_data.get('cod') == 200:  # Check if request was successful
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']

        print(f"\nWeather in {city}:")
        print(f"Temperature: {temp} °C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {description.capitalize()}")
    else:
        print(f"\nSorry, could not find weather data for '{city}'. Please check the city name.")
