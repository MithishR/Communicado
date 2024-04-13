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
from django.core.mail import send_mail
from django.conf import settings

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
                request.session['userRole'] = user.role
                request.session['userName'] = user.name
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
            
        send_mail(
            'Welcome to Communicado ',
            "Your account has been successfully created ! Welcome to Communicado "+name,
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False
        )
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
            return redirect('organizer_actions') 
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
        event.isVerified=False
        # event.imageURL = request.POST.get('image')
        event.save()

        success_message = "Updated event details sent to admin for approval."
        messages.success(request, success_message)
        return redirect('organizer_actions')  
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
    user=get_object_or_404(users,userID=request.session['userID'])

    if request.method == 'POST':
        # Retrieve the quantity from the form submission
        quantity = int(request.POST.get('quantity'))

        # Create a new BookedEvent object and save it to the database
        booked_event = BookedEvent(
            eventID=event,
            quantity=quantity,
            isPaid=False,  # Assuming the event is not paid immediately upon booking
            user=user  # Assuming the user is logged in
        )
        booked_event.save()
        # Optionally, you can add a success message or redirect the user to a confirmation page
       
        return redirect('payment')  # Redirect the user to the payment page after booking

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
            BookedEvent.objects.filter(user=request.session.get('userID')).update(isPaid=True)
            bookedwalaevent = BookedEvent.objects.filter(user=request.session.get('userID'))
            bookedwalaeventref = BookedEvent.objects.filter(user=request.session.get('userID')).last()
            eventslist =   bookedwalaevent.values_list('eventID',flat = True)
            bookedwalaeventkainfo = Events.objects.filter(eventID__in=eventslist).last() 
            organiserIDEvents = Events.objects.filter(eventID__in=eventslist)
            organsierID = organiserIDEvents.values_list('eventOrganizerID',flat=True).last()
            organiser = users.objects.filter(userID = organsierID).first()
            date_time_string = bookedwalaeventkainfo.eventDateTime.strftime("%Y-%m-%d %H:%M:%S")
            ID = request.session.get('userID')
            userbooking = get_object_or_404(users,userID = ID)
            send_mail(
            'Booking Confirmation ',
            " Hi "+userbooking.name+",Your Booking for "+bookedwalaeventkainfo.name +" on "+date_time_string +" in "+bookedwalaeventkainfo.location+" is confirmed!",
            'settings.EMAIL_HOST_USER',
            [userbooking.email],
            fail_silently=False
        )
            send_mail(
            'New Booking',
            " Hi a new booking has been made by "+userbooking.name+", for "+bookedwalaeventkainfo.name +" on "+date_time_string +" in "+bookedwalaeventkainfo.location+" is confirmed!",
            'settings.EMAIL_HOST_USER',
            [organiser.email],
            fail_silently=False
        )
            messages.success(request, 'Payment successful and Booking Confirmed! Please look out for a confirmation email with details of your booking.')
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
    success_message = "Event Approved. Added in the system."
    messages.success(request, success_message)
    return redirect('admin_actions')
    
    
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
    success_message = "Event Rejected. Not added in the system."
    messages.success(request, success_message)
    return redirect('admin_actions')

def confirmation(request):
    
    return render(request, "pages/confirmation.html")
    
def logout(request):
    request.session.flush()
    return render(request, "pages/logout.html")

def delete(request, event_ID):
    event = get_object_or_404(Events, eventID=event_ID)
    event.delete()
    success_message = "Event deleted successfully."
    messages.success(request, success_message)
    return redirect('admin_actions')


def remove(request):
    remove = Events.objects.filter(isVerified=1)
    return render(request, 'pages/remove.html', {'remove': remove})
def editacc(request):
    user_id = request.session.get('userID')
    user = users.objects.get(userID=user_id)
    return render(request , 'pages/editacc.html',{'user':user})
def edit(request):
    user_id = request.session.get('userID')
    user = get_object_or_404(users, userID = user_id)
    

    if request.method == 'POST':
        user.name =  request.POST.get('name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.address = request.POST.get('address')
        user.save()
    

    return render (request,'pages/edit.html')
def delete_booking(request, event_ID):
    if request.method == 'POST':
        booked_event = get_object_or_404(BookedEvent, eventID=event_ID, user=request.session.get('userID'))
        booked_event.delete()
        success_message = "Event booking deleted successfully."
        messages.success(request, success_message)
        return redirect('userbookeventinfo')

