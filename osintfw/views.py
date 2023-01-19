from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def chartfw(request):
    return render(request, "osintfw/chartfw.html")
