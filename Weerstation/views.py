from django.shortcuts import render
from django.core.mail import send_mail
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
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            message_name, #subject
            message, #message
            message_email, #from email
            ['SmSi050804@leerling.mosa-rt.be'], #to Email
        )

        return render(request, "contact.html", {'message_name': message_name})
    else:
        return render(request, 'contact.html', {})




