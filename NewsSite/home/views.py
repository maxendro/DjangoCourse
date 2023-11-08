from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def contacts(request):
    return render(request, 'home/contacts.html')

def about(request):
    return render(request, 'home/about.html')

def signup(request):
    return render(request, 'home/signup.html')

def create(request):
    return render(request, 'home/create.html')