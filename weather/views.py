from django.shortcuts import render
import json
import urllib
# Create your views here.
def home(request):

    if request.method == 'POST':

        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=b26f584511a96e2b0cc0de1a88d86d92').read()
        json_data = json.loads(res)
        data={
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon'])+''+str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp'])+' K',
            "pressure":str(json_data['main']['pressure']),
            "humidity":str(json_data['main']['humidity']),
        }
    else:
        data ={}
    return render(request, 'index.html',data)

def test(request):
    
    return render(request,'test.html')