from django.shortcuts import render
from django.http import HttpResponse
from .models import News


def index(request):
    value = 10
    n1 = News('Новость 1', 'Текст 1',' 01.11.2023' )
    n2 = News('Новость 2', 'Текст 2', ' 07.11.2023')
    l = [n1,n2]

    # return HttpResponse("<h1>Главная страница</h1>")
    context = {'title': 'Главная страница',
               'Header1': 'Заголовок страницы',
               'value': value,
               'numbers': l

               }
    return render(request, 'main/index.html', context)
