from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Placeone


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    objj = Placeone.objects.all()
    return render(request, "index.html", {'result': obj, 'resultone': objj})

# def about(request):
#     return render(request, "about.html")
