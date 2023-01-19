from django.shortcuts import render
from django.http import HttpResponse
import requests




def home(request):
    return render(request, "home.html")


def removepunc(request):
    if request.method == 'GET':
        djtext = request.GET.get('text')
     
        respons1 = requests.get(
            'https://api.github.com/users/'+djtext).json() 
        respons = requests.get(
            'https://api.github.com/users/'+djtext+'/repos').json()
      

        if len(respons) > 2:
            resultList = list(respons[0] .values())  
            print(resultList[3])
      
            full_name = resultList[3]
            language = requests.get(
            'https://api.github.com/repos/'+full_name+'/languages').json()
     
            context = {'respons': respons,
                   'respons1': respons1, 'language': language}
            return render(request, "removepunc.html", context)
      
        else:
            return HttpResponse("User Not Found ")
    else:
          
        return HttpResponse("Something Wrong")
