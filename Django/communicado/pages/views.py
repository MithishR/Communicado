from django.shortcuts import render,redirect
<<<<<<< HEAD
from .models import *
from django.contrib.auth import authenticate, login as auth_login
from django.views.decorators.csrf import csrf_exempt
=======
from .models import users
from .models import events
# from django.contrib.auth import messages
from django.views.decorators.csrf import csrf_exempt 
>>>>>>> main
from django.db import connection

def home(request):
    return render(request, "pages/home.html", {})
def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM users where username = %s and password = %s",[username,password],)
            row = cursor.fetchone()
            count = row[0]
            if(count==1):
                return redirect('home')
            else: 
                error_message = "Invalid username or password."
                return render(request, 'pages/login.html', {'error_message': error_message})
            
    else:
        return render(request,'pages/login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        role=request.POST.get('role')
        address=request.POST.get('address')
        #user = users(role=role, username=username, email=email, address=address, password=password)
       # user.save()
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO users (role, username, email, address, password) VALUES (%s, %s, %s, %s, %s)",[role, username, email, address, password],)
        return redirect('login')
    else:
        return render(request, "pages/signup.html", {})

    # return render(request, "pages/signup.html", {})
def useracc(request):
    data = users.objects.all()
    context = {"users": data}
    return render (request,"pages/useraccount.html",context)
def event(request):
    data = Events.objects.all()
    context = {"events": data}
    return render (request , "pages/events.html",context)
def test_page(request):
    return render(request, "pages/test_page.html")

