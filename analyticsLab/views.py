from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def analyticsLab(request):
    return render(request, "analyticsLab/dashboard.html")

def searchDatabase(request):
    return render(request, "analyticsLab/searchDatabase.html")