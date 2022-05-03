from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    from weerdata.models import Weerdata
    objs = Weerdata.objects.all()
    print("objs", objs)
    return render(request, "index.html", {"objs": objs})

def dashboard(request):
    return render(request, "dashboard.html")

def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")



