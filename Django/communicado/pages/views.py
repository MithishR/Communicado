from django.shortcuts import render
from .models import users
from .models import events

def home(request):
    return render(request, "pages/home.html", {})
def login(request):
    return render(request, "pages/login.html", {})
def signup(request):
    return render(request, "pages/signup.html", {})
def useracc(request):
    data = users.objects.all()
    context = {"users": data}
    return render (request,"pages/useraccount.html",context)
def event(request):
    data = events.objects.all()
    context = {"events": data}
    return render (request , "pages/events.html",context)

