from django.shortcuts import render,redirect,get_object_or_404
from .models import *


def home(request):
    return render(request, "pages/home.html", {})
# def login(request):

#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         with connection.cursor() as cursor:
#             cursor.execute("SELECT COUNT(*) FROM users where username = %s and password = %s",[username,password],)
#             row = cursor.fetchone()
#             count = row[0]
#             if(count==1):
#                 return redirect('home')
#             else: 
#                 error_message = "Invalid username or password."
#                 return render(request, 'pages/login.html', {'error_message': error_message})
            
#     else:
#         return render(request,'pages/login.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = users.objects.get(username=username, password=password)
            # Authentication successful
            if user:
                # Redirect to home page or any other page you want
                success_message = "Welcome " + user.name  # Accessing name from the user object
                return render(request, 'pages/home.html', {'success_message': success_message})
                
            else:
                error_message = "Invalid username or password."
                return render(request, 'pages/login.html', {'error_message': error_message})
        except users.DoesNotExist:
            error_message = "Invalid username or password."
            return render(request, 'pages/login.html', {'error_message': error_message})
    else:
        return render(request, 'pages/login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        role=request.POST.get('role')
        address=request.POST.get('address')
        user = users(role=role, name = name, username=username, email=email, address=address, password=password)
        user.save()
        success_message = "User Account Created for: " + user.name  # Accessing name from the user object
        return render(request, 'pages/login.html', {'success_message': success_message})
        
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
def eventinfo(request,event_ID):
    event = get_object_or_404(Events,eventID=event_ID)
    return render(request, 'pages/i.html', {'event': event})

