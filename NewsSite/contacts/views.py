from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def contacts (request):
    #return HttpResponse("<h1>Contacts</h1>")
    return render(request, 'main/contacts.html')

