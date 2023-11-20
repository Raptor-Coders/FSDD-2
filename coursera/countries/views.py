from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def country(request):
    return HttpResponse("This is the countries and cities app")
