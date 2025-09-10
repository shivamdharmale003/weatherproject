from django.shortcuts import render
import datetime
import requests

# Create your views here.
def home(request):
    city = 'pune'  # default city

    if request.method == 'POST' and 'city' in request.POST:
        city = request.POST['city']

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=f6e858555a76b314da9dcddf24ab8c0a'
    params = {'units': 'metric'}



    try:
        response = requests.get(url, params=params)
        data = response.json()

        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        day = datetime.date.today()

        return render(request, "index.html", {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city
        })
    except:
        return render(request, "index.html", {
            'city': city,
            'error': 'City not found'
        })