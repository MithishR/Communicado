import datetime
from unicodedata import numeric
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.hashers import make_password,check_password
from .models import *
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Events , BookedEvent
from django.db import connection
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import *
from django.db.models import Q
from django.shortcuts import redirect

def home(request):
    return render(request, "pages/home.html")


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = users.objects.get(username=username)
            if check_password(password, user.password):
                request.session['userID'] = user.userID
                #request.session.set_test_cookie() 
                if user.role == 'EventOrganizer':
                    success_message = "Welcome " + user.name + ", userid:"+ str(user.userID) # Accessing name from the user object
                    messages.success(request, success_message)
                    return redirect('organizer_actions')
                elif user.role == 'Admin':
                    return redirect('admin_actions')
                
                else:
                    success_message = "Welcome " + user.name + ", userid:"+ str(user.userID) # Accessing name from the user object
                    messages.success(request, success_message)
                    return redirect('home')
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
        event_organizer = None
        try:
            name = request.POST.get('name')
            user_id = request.session.get('userID')
            user = users.objects.get(userID=user_id)
            if user.role.__eq__('EventOrganizer'):
                event_organizer = EventOrganizer.objects.get(user=user)
            else:
                raise Exception("User is not an Event Organizer")
            print(event_organizer)
            name = request.POST.get('name')
            eventDateTime = request.POST.get('eventDateTime')
            location = request.POST.get('location')
            capacity = request.POST.get('capacity')
            category = request.POST.get('category')
            artist = request.POST.get('artist')
            image=request.POST.get('image')
            price=request.POST.get('price')
        
            new_event = Events(name=name, eventDateTime=eventDateTime, location=location, capacity=capacity,
                            category=category, artist=artist, isVerified=False, eventOrganizerID=event_organizer, imageURL=image,price=price)
            new_event.save()
            success_message = "Event added successfully. It is pending approval."
            messages.success(request, success_message)
            return redirect('home') 
        except Exception as e:
            error_message = f"An error occurred while adding the event. Role of user: {users.objects.get(userID=request.session.get('userID')).role}. Type of user: {type(request.session.get('user_id'))}. Error: {str(e)}"
            messages.error(request, error_message)
            return redirect('add_event')
    else:
        return render(request, 'pages/add_event.html')

def useracc(request):
    userID = request.session.get('userID')
    
    
    if not userID:
        error_message = "You aren't logged in. Kindly log in and try again."
        return render(request, "pages/useraccount.html", {'error_message': error_message})
    else:
        usercurrentlyloggedin = users.objects.filter(userID=userID).first()
        
        return render(request, "pages/useraccount.html", {'user': usercurrentlyloggedin})


def event(request):
    data = Events.objects.filter(isVerified=1)
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
                data = Events.objects.filter(isVerified=1)
                context = {"events": data ,
                'unique_categories': unique_categories,
                'error_message': error_message
                }
                return render (request , "pages/events.html",context)
                
        else:
            data=Events.objects.filter(category=category, isVerified=1)
            context = {"events": data ,
                'unique_categories': unique_categories}
    else:
        if search_query and search_query != " ":
            data = Events.objects.filter(
            Q(artist__icontains=search_query) |
            Q(name__icontains=search_query))
            if(data.count() == 0):
                error_message = "No Matches for "+ search_query+" :( Currently available Events: "
                data = Events.objects.filter(isVerified=1)
                context = {"events": data ,
                'unique_categories': unique_categories,
                'error_message': error_message
                }
                return render (request , "pages/events.html",context)
        else:
            data=Events.objects.filter(isVerified=1)
           
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
    user_id = request.session.get('userID')
    user = users.objects.get(userID=user_id)
    
    if user.role.__eq__('EventOrganizer'):
        try:
            event_organizer = EventOrganizer.objects.get(user=user)
            events = Events.objects.filter(eventOrganizerID=event_organizer)
            return render(request, 'pages/edit_event.html', {'events': events})
        except EventOrganizer.DoesNotExist:
            error_message = "You are not authorized to access this page."
            return render(request, 'error.html', {'error_message': error_message})


    else:
        error_message = f"An error occurred while retrieving the event. Role of user: {users.objects.get(userID=request.session.get('user_id')).role}. Type of user: {type(request.session.get('user_id'))}. Error: {str(e)}"
        messages.error(request, error_message)
        return redirect('edit_event')

    
def change_event(request, event_ID):
    event = get_object_or_404(Events, eventID=event_ID)
    if request.method == 'POST':
        event.name = request.POST.get('name')
        event.eventDateTime = request.POST.get('eventDateTime')
        event.location = request.POST.get('location')
        event.capacity = request.POST.get('capacity')
        event.category = request.POST.get('category')
        event.artist = request.POST.get('artist')
        event.price = request.POST.get('price')
        # event.imageURL = request.POST.get('image')
        event.save()

        success_message = "Event updated successfully."
        messages.success(request, success_message)
        return redirect('home')  
    else:
        # Render the form template with the event data for editing
        return render(request, 'pages/change_event.html', {'event': event})


def userbookeventinfo(request):
    user_id = request.session.get('userID')
    if not user_id:
        error_message = "You aren't logged in. Kindly log in and try again."
        return render(request, 'pages/userbookinghistory.html', {'error_message': error_message, 'show_login_button': True})
    else:

        booked_events = BookedEvent.objects.filter(user=user_id)
        if booked_events.count() == 0 :
            no_events_message = "You currently have no booked events. Book now!"
            return render(request, 'pages/userbookinghistory.html', {'no_events_message': no_events_message, 'show_events_button': True})
        else:
            eventslist =   booked_events.values_list('eventID',flat = True)
            events = Events.objects.filter(eventID__in=eventslist)
            return render(request, 'pages/userbookinghistory.html', {'events': events})

        
       
def add_to_cart(request, event_ID):
    # Check if the user is logged in (assuming you're storing user_id in the session)
    if not request.session.get('userID'):
        messages.add_message(request, messages.INFO, 'Please log in to continue.')
        return redirect('login')  # Update 'login_url_name' with your login route's name

    event = get_object_or_404(Events, eventID=event_ID)

    if request.method == 'POST':

        # Here, you would normally add the event to the user's cart.
        # Since you don't have a Cart model yet, let's simulate it with session (temporary solution)

        # Check if a cart exists in session, if not, create one
        if 'cart' not in request.session or not request.session['cart']:
            request.session['cart'] = []

        # Add the event ID to the session cart
        request.session['cart'].append(event_ID)
        # Important: mark the session as modified to make sure it gets saved
        request.session.modified = True

        messages.success(request, 'Event added to cart successfully!')
        return redirect('cart')  # Update 'cart' with your cart route's name or wherever you want to redirect the user

    # If it's not a POST request, just render the add_to_cart page
    return render(request, 'pages/add_to_cart.html', {'event': event})

def payment(request):
    
    if request.method == 'POST':
        # Extract card details from the form
        card_number = request.POST.get('card_number')
        expiration_date = request.POST.get('expiration_date')
        cvv = request.POST.get('cvv')
        cardholder_name = request.POST.get('cardholder_name')
        
        try:
            # Basic validation for card number
            if len(card_number) != 16 or not card_number.isdigit():
                raise ValueError('Invalid card number')
            
                
            # Basic validation for CVV
            if len(cvv) != 3 or not cvv.isdigit():
                raise ValueError('Invalid CVV')

            # Basic validation for cardholder name
            if not cardholder_name.strip():
                raise ValueError('Cardholder name cannot be empty')

            # If all validations pass, simulate a successful payment
            messages.success(request, 'Payment successful!')
            return redirect('confirmation')
        except Exception as e:
            # Payment failed, display an error message
            messages.error(request, f'Payment failed: {str(e)}')
            return redirect('payment')

    return render(request, 'pages/payment.html')

def admin_actions(request):
    userData = users.objects.all()
    context = {"userData": userData, }
    return render (request,"pages/admin_actions.html",context)

def pending(request):
    pending = Events.objects.filter(isVerified=0)
    return render(request, 'pages/pending.html', {'pending': pending})

    
def rejected(request):
    rejected = Events.objects.filter(isVerified=-1)
    return render(request, 'pages/rejected.html', {'rejected': rejected})
def eventaction(request,event_ID):
    event = get_object_or_404(Events,eventID=event_ID)
    return render(request, 'pages/eventaction.html', {'event': event})


def approve_event(request, event_ID):
    event = get_object_or_404(Events,eventID=event_ID)
    user_id = request.session.get('userID')
    user = users.objects.get(userID=user_id)
    if user.role.__eq__('Admin'):
        admin = Admin.objects.get(user=user)
    else:
        raise Exception("User is not an Event Organizer")
    event.adminID=admin
    event.isVerified = 1 
    event.save()
    return redirect('pending')
    
def reject_event(request, event_ID):
    event = get_object_or_404(Events,eventID=event_ID)
    user_id = request.session.get('userID')
    user = users.objects.get(userID=user_id)
    if user.role.__eq__('Admin'):
        admin = Admin.objects.get(user=user)
    else:
        raise Exception("User is not an Event Organizer")
    event.adminID=admin
    event.isVerified = -1  
    event.save()
    return redirect('pending')

def confirmation(request):
    return render(request, "pages/confirmation.html")
    
