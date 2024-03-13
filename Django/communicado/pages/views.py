from django.shortcuts import render,redirect
from .models import users
from .models import events
from django.contrib.auth import authenticate, login as auth_login
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, "pages/home.html", {})
def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Redirect to home page after successful login
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        return redirect('login')
    else:
        return render(request, "pages/signup.html", {})

    # return render(request, "pages/signup.html", {})
def useracc(request):
    data = users.objects.all()
    context = {"users": data}
    return render (request,"pages/useraccount.html",context)
def event(request):
    data = events.objects.all()
    context = {"events": data}
    return render (request , "pages/events.html",context)
def test_page(request):
    return render(request, "pages/test_page.html")


