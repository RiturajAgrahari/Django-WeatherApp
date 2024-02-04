import datetime

import requests
import os
from dotenv import load_dotenv
from django.shortcuts import render, redirect
from django.contrib import messages

# CONTAINS ONLY 1 BUG!

# Create your views here.

load_dotenv()

def index(request):
    # API_KEY = open("../api keys/weather app key/API_KEY", "r").read()
    API_KEY = os.getenv("TOKEN")
    current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    forecast_url = "https://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&appid={}"

    if request.method == 'POST':
        city1 = request.POST['city1']
        city2 = request.POST.get('city2', None)

        weather_data1, daily_forecast1, message1 = fetch_weather_and_forecast(city1, API_KEY, current_weather_url, forecast_url)

        if city2:
            weather_data2, daily_forecast2, message2 = fetch_weather_and_forecast(city2, API_KEY, current_weather_url,
                                                                        forecast_url)

        else:
            weather_data2, daily_forecast2, message2 = None, None, None

        context = {
            "weather_data1": weather_data1,
            "daily_forecast1": daily_forecast1,
            "weather_data2": weather_data2,
            "daily_forecast2": daily_forecast2,
            "heading": "5-Day Forecast"
        }

        if message1 is not None:
            messages.success(request, message1)
            context["weather_data1"] = None
            context["daily_forecast1"] = None

        if message2 is not None:
            messages.success(request, message2)
            context["weather_data2"] = None
            context["daily_forecast2"] = None

        return render(request, 'index.html', context)


    else:
        return render(request, 'index.html', {'heading': "Check or Compare Weather"})


def fetch_weather_and_forecast(city, api_key, current_weather_url, forecast_url):
    response = requests.get(current_weather_url.format(city, api_key)).json()

    if response['cod'] == 200:
        lat, lon = response['coord']['lat'], response['coord']['lon']
        forecast_response = requests.get(forecast_url.format(lat, lon, api_key)).json()

        weather_data = {
            "city": city,
            "temperature": round(response['main']['temp'] - 273.15, 2),
            "description": response['weather'][0]['description'],
            "icon": response['weather'][0]['icon']
        }

        daily_forecast = []
        for i in range(0, len(forecast_response['list']), 8):
            daily_data = forecast_response['list'][i]
            daily_forecast.append({
                "day": datetime.datetime.fromtimestamp(daily_data['dt']).strftime("%A"),
                "min_temp": round(daily_data['main']['temp_min'] - 273.15, 2),
                "max_temp": round(daily_data['main']['temp_max'] - 273.15, 2),
                "description": daily_data['weather'][0]['description'],
                "icon": daily_data['weather'][0]['icon']
            })

        return weather_data, daily_forecast, None

    elif response['cod'] == "404":
        return None, None, response['message'].capitalize()

    else:
        print('Something went wrong!')
        print(response['message'].capitalize())
        return None, None, None