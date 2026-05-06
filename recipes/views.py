from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Home in view")

def about(request):
    return HttpResponse("Sobre in view")

def contact(request):
    return HttpResponse("Contato in view")