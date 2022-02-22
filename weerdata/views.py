from django.shortcuts import render
from django.http import HttpResponse
from .models import Weerdata

def stuurdata(request):
    temp = request.GET["temperatuur"]
    druk = request.GET["luchtdruk"]
    vochtigheid = request.GET["luchtvochtigheid"]
    w = Weerdata(temperatuur = temp, luchtdruk = druk, luchtvochtigheid = vochtigheid)
    w.save()
    return HttpResponse(f"OK alles ok {temp}{druk}{vochtigheid}")
