from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    #return HttpResponse("<h1>Главная страница</h1>")
    return render(request, 'main/index.html')
