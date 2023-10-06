from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    my_api = 'e77685b5f09c8584635705766baaa256'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + my_api

    # city = 'London'
    # res = requests.get(url.format(city)).json()

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all().order_by('-id')[:1]

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': round(res["main"]["temp"]),
            'pressure': res["main"]["pressure"],
            'wind': res['wind']['speed'],
            'icon': res['weather'][0]['icon']
        }

        all_cities.append(city_info)

    # context = {'city_info': city_info, 'form': form}
    context = {'all_info': all_cities,
                'form': form}

    return render(request, 'weather/index.html', context)