from django.shortcuts import render
from .utils import get_city, weather


# Create your views here.
def index(request):
    return render(request, "weather/index.html")

def button(request):
    return render(request, "weather/button.html")


def check(request):
    if request.method == "POST":

        data = request.POST["location"]

        location = get_city(data)
    
        details = weather(location["lat"], location["lon"])

        return render(request, "weather/weather.html", {"details": details, "location": data})

