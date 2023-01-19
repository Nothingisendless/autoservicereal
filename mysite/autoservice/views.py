from django.shortcuts import render
from django.http import HttpResponse
from .models import AutomobilioModelis, Automobilis, Paslauga, Uzsakymas

def index(request):
    return HttpResponse("Labas pasauli")
