from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def contacts(request):
    return render(request, 'home/contacts.html')

def about(request):
    return render(request, 'home/about.html')

def signup(request):
    return render(request, 'home/signup.html',{"sform":UserCreationForm})

def create(request):
    return render(request, 'home/create.html')