from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.hashers import make_password,check_password
from .models import *
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Events 

from django.contrib.auth.models import *
from django.db.models import Q


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

                if user.role == 'EventOrganizer':
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
        encrypted_password = make_password(password)
        phoneNumber=request.POST.get('phoneNumber')
        user = users(role=role, name = name, username=username, email=email, address=address, password=encrypted_password)
        user.save()
        if role.__eq__('EventOrganizer'):
            event_organizer = EventOrganizer(user=user, phoneNumber=phoneNumber)
            event_organizer.save()
        success_message = "User Account Created for: " + user.name
        return render(request, 'pages/login.html', {'success_message': success_message})
        
    else:
        return render(request, "pages/signup.html", {})

    # return render(request, "pages/signup.html", {})
    
def add_event(request):
    if request.method == 'POST':
        try:
            # organizer_name = request.POST.get('event_organizer')
            # event_organizer = EventOrganizer.objects.get(user__name=organizer_name)

            name = request.POST.get('name')
            # event_organizer_id = users.userID
            eventDateTime = request.POST.get('eventDateTime')
            location = request.POST.get('location')
            capacity = request.POST.get('capacity')
            category = request.POST.get('category')
            artist = request.POST.get('artist')
            image=request.POST.get('image')
        
            new_event = Events(name=name, eventDateTime=eventDateTime, location=location, capacity=capacity,
                            category=category, artist=artist, isVerified=False, imageURL=image)
            new_event.save()
            success_message = "Event added successfully. It is pending approval."
            messages.success(request, success_message)
            return redirect('home')  # Redirect to home page or any other appropriate page after adding event
        except Exception as e:
            error_message = "An error occurred while adding the event: {}".format(str(e))
            messages.error(request, error_message)
            return redirect('add_event')
    else:
        return render(request, 'pages/add_event.html')

def useracc(request):
    data = users.objects.all()
    context = {"users": data}
    return render (request,"pages/useraccount.html",context)
def event(request):
    data = Events.objects.all()
    unique_categories = Events.objects.values_list('category', flat=True).distinct()
    category = request.GET.get('category')
    search_query = request.GET.get('search')
    if (category and category != 'All Categories'):
        if search_query and search_query != " ":
            data = Events.objects.filter(
            Q(artist__icontains=search_query) |
            Q(name__icontains=search_query) |
            Q(category__icontains=search_query))
            if(data.count() == 0):
                error_message = "No Matches for "+ search_query+" :( Currently available Events: "
                data = Events.objects.all()
                context = {"events": data ,
                'unique_categories': unique_categories,
                'error_message': error_message
                }
                return render (request , "pages/events.html",context)
                
        else:
            data=Events.objects.filter(category=category)
            context = {"events": data ,
                'unique_categories': unique_categories}
    else:
        if search_query and search_query != " ":
            data = Events.objects.filter(
            Q(artist__icontains=search_query) |
            Q(name__icontains=search_query) )
            if(data.count() == 0):
                error_message = "No Matches for "+ search_query+" :( Currently available Events: "
                data = Events.objects.all()
                context = {"events": data ,
                'unique_categories': unique_categories,
                'error_message': error_message
                }
                return render (request , "pages/events.html",context)
        else:
            data=Events.objects.all()
           
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
    

def edit_event(request):
    events = Events.objects.all()  
    return render(request, 'pages/edit_event.html', {'events': events})

from django.http import HttpResponseBadRequest

# def change_event(request, event_ID):
#     event = get_object_or_404(Events, eventID=event_ID)
#     if request.method == 'POST':
#         event.name = request.POST.get('name')
#         event.eventDateTime = request.POST.get('eventDateTime')
#     return render(request, 'pages/change_event.html', {'event': event})
    
def change_event(request, event_ID):
    event = get_object_or_404(Events, eventID=event_ID)
    if request.method == 'POST':
        event.name = request.POST.get('name')
        event.eventDateTime = request.POST.get('eventDateTime')
        event.location = request.POST.get('location')
        event.capacity = request.POST.get('capacity')
        event.category = request.POST.get('category')
        event.artist = request.POST.get('artist')
        # event.imageURL = request.POST.get('image')
        event.save()

        success_message = "Event updated successfully."
        messages.success(request, success_message)
        return redirect('home')  
    else:
        # Render the form template with the event data for editing
        return render(request, 'pages/change_event.html', {'event': event})
    
    

def add_to_cart(request, event_ID):
    event = get_object_or_404(Events, eventID=event_ID)
    # Logic for adding item to cart
    if request.method == 'POST':
        # Handle form submission here
        # For example, you can create a CartItem object and save it to the database
        # cart_item = CartItem.objects.create(event=event, quantity=request.POST['quantity'])
        # Redirect the user after adding to cart
        return redirect('cart')
    return render(request, 'pages/add_to_cart.html', {'event': event})
