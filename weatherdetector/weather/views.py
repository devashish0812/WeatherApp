from django.shortcuts import render
import json
import urllib.request
# Create your views here.
def index(request):
    if request.method== 'POST':
        city=request.POST['city']
        print(city)
        res=urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q=" + str(city) + "&appid=30b8783933ad6f9441f89a717eeed88c").read()
        print(res)
        json_data=json.loads(res)
        data={
            "country_code" :str(json_data['sys']['country']),
            "latitude" :str(json_data['coord']['lat']),
            "longitude" :str(json_data['coord']['lon']),
            "temp": str(json_data['main']['temp']),
            "humidity": str(json_data['main']['humidity']),
        }
    else:
        city=' '
        data={}
    return render(request,'index.html',{'city': city, 'data': data})