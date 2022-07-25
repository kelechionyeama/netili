# Write functions for weather app
import requests
import urllib.parse


def get_city(city):
    """Look up City"""

    #Contact API
    try:
        url = f"http://api.openweathermap.org/geo/1.0/direct?q={urllib.parse.quote_plus(city)}&limit=5&appid=9a1c5c36ce12ab2b5fc08fd0d1abdac3"
        response = requests.get(url)
        response.raise_for_status()

    except requests.RequestException:
        return None

    #Parse/Work with response and get lat and lon
    """Get lat and lon"""

    quote = response.json()[0]
    return {
        "lat": quote["lat"],
        "lon": quote["lon"]
    }


def weather(lat, lon):
    headers = {
    'User-Agent': "neliti.com anton@neliti.com"
    } 

    try:
        url = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={lat}&lon={lon}"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except:
        print("error")

