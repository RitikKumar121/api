from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.


def home(request):
    return render(request, "home.html")


def removepunc(request):
    if request.method=='GET':
        djtext = request.GET.get('text')
        #analyze = djtext.upper()
    #    print(djtext)
        # params={'removetext':analyze}
        #print("chut")https://api.github.com/repos/RitikKumar121/blog/languages
        respons1 = requests.get(
            'https://api.github.com/users/'+djtext).json() #user name ko link ke sath jorne ke liye ayese kiye hai
        respons = requests.get(
        'https://api.github.com/users/'+djtext+'/repos').json()
        #respons is list type which is conatin dictionary as a element
        resultList = list(respons[0] .values())#conversion dict to list
        print(resultList[3])
        #print(type(resultList))
        full_name =resultList[3]
        language = requests.get(
            'https://api.github.com/repos/'+full_name+'/languages').json()
        if len(respons)>2:
            # for multiple context pass karne ke liye
            context = {'respons': respons,
                       'respons1': respons1, 'language': language}
            return render(request, "removepunc.html", context)
            # return render(request,"removepunc.html",params)
        else:
            return HttpResponse("User Not Found ")
    else:
    #    print("hh")
        return HttpResponse("Something Wrong")
