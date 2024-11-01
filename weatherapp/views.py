# import urllib.request
# import json
# from django.shortcuts import render
# # Create your views here.


# def index(request):

#     if request.method == 'POST':
#         city = request.POST['city']

#         source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=9ed04f720a3537bbd153fee0dfc01378').read()
#         list_of_data = json.loads(source)
 
#         data = {
#             "country_code": str(list_of_data['sys']['country']),
#             "coordinate": str(list_of_data['coord']['lon']) + ', '
#             + str(list_of_data['coord']['lat']),

#             "temp": str(list_of_data['main']['temp']) + ' °C',
#             "pressure": str(list_of_data['main']['pressure']),
#             "humidity": str(list_of_data['main']['humidity']),
#             'main': str(list_of_data['weather'][0]['main']),
#             'description': str(list_of_data['weather'][0]['description']),
#             'icon': list_of_data['weather'][0]['icon'],
#         }
#         print(data)
#     else:
#         data = {}

#     return render(request, "main/index.html", data)




from django.shortcuts import render, redirect
import requests
from geopy.geocoders import Nominatim
from .forms import LocationForm, MemberForm
from .models import WeatherAlert, Member
from django.http import JsonResponse
from django.conf import settings


API_KEY = '798aec6504e12e9234e998db8e2be601'

api_key = settings.OPENWEATHER_API_KEY

def get_weather_data(location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()


# def check_weather(request):
#     if request.method == 'POST':
#         # Logic to fetch and display weather
#         weather_data = {
#             'temperature': 25,
#             'condition': 'Sunny',
#         }
#         return JsonResponse(weather_data)
#     return JsonResponse({'error': 'Invalid request'}, status=400)

def check_weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')  # Assuming you are submitting a city from the form

        # Replace with your actual API key from OpenWeatherMap
        ##api_key = settings.OPENWEATHER_API_KEY
        weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        # Make the request to OpenWeatherMap API
        response = requests.get(weather_url)
        if response.status_code == 200:
            data = response.json()
            
            # Parse the weather data
            weather_data = {
                'temperature': data['main']['temp'],
                'condition': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'pressure': data['main']['pressure'],
                'name': data['name']  # City name
            }

            return JsonResponse(weather_data)
        else:
            return JsonResponse({'error': 'City not found'}, status=404)

    return JsonResponse({'error': 'Invalid request'}, status=400)


def index(request):
    # Use Geolocation or Manual Input
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            weather_data = get_weather_data(city)
    else:
        # Use geolocation (dummy coordinates here for example)
        city = "New York"
        weather_data = get_weather_data(city)
        form = LocationForm()

    context = {
        'form': form,
        'weatherapp': weather_data,
    }
    return render(request, 'weatherapp/index1.html', context)

def add_alert(request):
    if request.method == 'POST':

        print(request.POST)

        location = request.POST['location']
        alert_type = request.POST['alert_type']
        threshold = request.POST['threshold']
        user_email = request.POST['user_email']
        # temperature = request.POST.get('temperature')
        # condition = request.POST.get('condition')
        # humidity = request.POST.get('humidity')
        # wind_speed = request.POST.get('wind speed')
        # air_pressure = request.POST.get('air pressure')
        # timestamp = request.POST.get('timestamp')

        WeatherAlert.objects.create(location=location, alert_type=alert_type, threshold=threshold, user_email=user_email)
        return redirect('index1')
    

def add_member(request):
    if request.method =='POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect("/")
            return redirect("membersList")
        
    else:
        form = MemberForm()

    return render(request, 'weatherapp/addMember.html', {'form': form})


def members_list(request):
    members = Member.objects.all()
    return render(request, 'weatherapp/membersList.html', {'members': members})
  