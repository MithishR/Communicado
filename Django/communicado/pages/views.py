from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.hashers import make_password,check_password
from .models import *
from django.contrib import messages


def home(request):
    return render(request, "pages/home.html")


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = users.objects.get(username=username)
            
            # Check if the entered password matches the hashed password in the database
            if check_password(password, user.password):
                # Authentication successful

                if user.role == 'organiser':
                    success_message = "Welcome " + user.name
                    messages.success(request, success_message)
                    return redirect('organizer_actions')
                    #return render(request, 'pages/organizer_actions.html', {'success_message': success_message})
                else:
                    success_message = "Welcome " + user.name  # Accessing name from the user object
                    messages.success(request, success_message)
                    return redirect('home')
                 #   return render(request, 'pages/home.html', {'success_message': success_message})
            else:
                error_message = "Invalid username or password."
                return render(request, 'pages/login.html', {'error_message': error_message})
        except user.DoesNotExist:
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
        
        # Encrypt the password
        encrypted_password = make_password(password)
        
        user = users(role=role, name = name, username=username, email=email, address=address, password=encrypted_password)
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
    unique_categories = Events.objects.values_list('category', flat=True).distinct()
    category = request.GET.get('category')
    if category and category != 'All Categories':
        data=Events.objects.filter(category=category)
        context = {"events": data ,
                'unique_categories': unique_categories}
        
    else:
    
        context = {"events": data ,
                'unique_categories': unique_categories}
    return render (request , "pages/events.html",context)
def test_page(request):
    return render(request, "pages/test_page.html")
def eventinfo(request,event_ID):
    event = get_object_or_404(Events,eventID=event_ID)
    return render(request, 'pages/i.html', {'event': event})
def xyz(request):
    data = users.objects.all()
    context = {"xyz": data}
    return render (request,"pages/xyz.html",context)

def organizer_actions(request):
    userData = users.objects.all()
    context = {"userData": userData, }
    return render (request,"pages/organizer_actions.html",context)
    
def add_event(request):
    return render(request, 'pages/add_event.html')

def edit_event(request):
    return render(request, 'pages/edit_event.html')

