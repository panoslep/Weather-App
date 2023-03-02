import requests
import config

# Prompt the user to enter a city or zip code
# location = input("Please enter location")
lat = 52.197584649999996
lon = 0.13915373736874398

# Build the URL to make the API request
url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={config.API_KEY}'

# Make the API request and get the response
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data from the response
    data = response.json()

    # Extract the relevant weather data from the JSON response
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']

    # Display the weather data to the user
    print(f"Temperature: {round(temp-273.15)} C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description}")
else:
    print("Error fetching weather data.")
