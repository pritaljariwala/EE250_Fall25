import requests
import json

# WeatherAPI key
WEATHER_API_KEY = '1766237c54e345509cb145814252309'  # TODO: Replace with your own WeatherAPI key

def get_weather(city):
    # TODO: Build the API request URL using the base API endpoint, the API key, and the city name provided by the user.
    base_url = "http://api.weatherapi.com/v1/current.json"
    request_url = f"{base_url}?key={WEATHER_API_KEY}&q={city}"

    # TODO: Make the HTTP request to fetch weather data using the 'requests' library.
    response = requests.get(request_url)

    # TODO: Handle HTTP status codes:
    # - Check if the status code is 200 (OK), meaning the request was successful.
    # - If not 200, handle common errors like 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), and any other relevant codes.
    
    if response.status_code == 200:
        # TODO: Parse the JSON data returned by the API. Extract and process the following information:
        # - Current temperature in Fahrenheit
        # - The "feels like" temperature
        # - Weather condition (e.g., sunny, cloudy, rainy)
        # - Humidity percentage
        # - Wind speed and direction
        # - Atmospheric pressure in mb
        # - UV Index value
        # - Cloud cover percentage
        # - Visibility in miles

        json_data = response.json()
        city = json_data['location']['name']
        temp_f = json_data['current']['temp_f']
        feels_like_f = (json_data['current']['feelslike_c'] * 9/5) + 32
        weather_condition = json_data['current']['condition']['text']
        humidity_percentage = json_data['current']['humidity']
        wind_speed = json_data['current']['wind_kph']
        wind_direction = json_data['current']['wind_dir']
        pressure = json_data['current']['pressure_mb']
        uv_index = json_data['current']['uv']
        cloud_cover = json_data['current']['cloud']
        visibility = json_data['current']['vis_km'] * 0.621

        # TODO: Display the extracted weather information in a well-formatted manner.
        print(f"Weather data for {city}...\n")
        print(f"Temperature: {temp_f} degrees Fahrenheit")
        print(f"Feels like: {feels_like_f} degrees Fahrenheit")
        print(f"Weather condition: {weather_condition}")
        print(f"Humidity Percentage: {humidity_percentage}%")
        print(f"Wind speed: {wind_speed} kph {wind_direction}")
        print(f"Pressure: {pressure} mb")
        print(f"UV index: {uv_index}")
        print(f"Cloud cover: {cloud_cover}")
        print(f"Visibility: {visibility} miles")

    else:
        if response.status_code == 400:
            print(f"Error: {response.status_code}. Bad Request")
        if response.status_code == 401: 
            print(f"Error: {response.status_code}. Unauthorized")
        if response.status_code == 403: 
            print(f"Error: {response.status_code}. Forbidden")
        if response.status_code == 404:
            print(f"Error: {response.status_code}. Not found")

        

if __name__ == '__main__':
    city_name = input("Enter city name: ")
    get_weather(city_name)
    pass
