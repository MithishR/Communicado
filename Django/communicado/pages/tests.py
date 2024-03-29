import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse 
from .models import *
from django.test import LiveServerTestCase
from django.contrib.auth.hashers import make_password
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options
import time

# Example 1

#class Hosttest(LiveServerTestCase):
  	
#	def testhomepage(self):
#		options = Options()
#		options.headless = True
#		driver = webdriver.Chrome(options=options)
#		driver.get(self.live_server_url)
				# try driver.get(self.live_server_url) if driver.get('http://127.0.0.1:8000/') does not work	
#		assert "Hello, world!" in driver.title
            
class UsersTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = users.objects.create(
            username='testuser123',
            password='password123',
            name='TestUser',
            role='Admin',
            email='email@example.com',
            address='123 Main St, City, Country'
        )
        cls.user.save()

        cls.admin = Admin.objects.create(
            user=cls.user,
            officeNo='A123'
        )
        cls.admin.save()

        cls.organizer_user = users.objects.create(
        username='organizer123',
        password='organizerpass',
        name='Organizer User',
        role='EventOrganizer',
        email='organizer@example.com',
        address='456 Organizer St, City, Country'
        )
        cls.organizer_user.save()

        cls.event_organizer = EventOrganizer.objects.create(
        user=cls.organizer_user,
        phoneNumber='123456789'
    )
        cls.event_organizer.save()

        cls.event_organizer = EventOrganizer.objects.create(
            user=users.objects.create(
                username='testorganizer123',
                password='password123',
                name='TestOrganizer',
                role='Organizer',
                email='organizer@example.com',
                address='456 Event St, City, Country'
            ),
            phoneNumber='123456789'
        )
        cls.event_organizer.save()
        

        cls.customer = Customer.objects.create(
            user=users.objects.create(
                username='testcustomer123',
                password='password123',
                name='TestCustomer',
                role='Customer',
                email='customer@example.com',
                address='789 Customer St, City, Country'
            ),
            phoneNumber='987654321'
        )
        cls.customer.save()

        cls.event = Events.objects.create(
            name='Test Event',
            eventDateTime=datetime.datetime.now(),
            location='Test Location',
            capacity=100,
            category='Test Category',
            artist='Test Artist',
            isVerified=True,
            adminID=cls.admin,
            eventOrganizerID=cls.event_organizer,
            imageURL='test_image.jpg',
            
        )
        cls.event.save()

        cls.booked_event = BookedEvent.objects.create(
            eventID=cls.event,
            quantity=2,
            isPaid=True,
            user=cls.user,
            referenceNumber="REF123"
        )

    def test_user_creation(self):
        user = self.user
        self.assertEqual(user.name, 'TestUser')
        self.assertEqual(user.role, 'Admin')
        self.assertEqual(user.email, 'email@example.com')

    def test_user_update(self):
        updated_data = {
            'name': 'Updated Name',
            'role': 'Updated Role',
            'email': 'updated@example.com',
            'address': 'Updated Address',
        }
        self.user.name = updated_data['name']
        self.user.role = updated_data['role']
        self.user.email = updated_data['email']
        self.user.address = updated_data['address']
        self.user.save()

        self.user.refresh_from_db()

        self.assertEqual(self.user.name, updated_data['name'])
        self.assertEqual(self.user.role, updated_data['role'])
        self.assertEqual(self.user.email, updated_data['email'])
        self.assertEqual(self.user.address, updated_data['address'])

    def test_user_deletion(self):
        user = self.user
        user.delete()

        with self.assertRaises(users.DoesNotExist):
            users.objects.get(username='testuser123')

    def test_booked_event_creation(self):
        booked_event = self.booked_event
        self.assertEqual(booked_event.quantity, 2)

    def test_booked_event_update(self):
        updated_quantity = 3
        booked_event = self.booked_event
        booked_event.quantity = updated_quantity

        booked_event.save()
        booked_event.refresh_from_db()
        self.assertEqual(booked_event.quantity, updated_quantity)

    def test_booked_event_deletion(self):
        booked_event = self.booked_event
        booked_event.delete()

        with self.assertRaises(BookedEvent.DoesNotExist):
            BookedEvent.objects.get(eventID=self.event)

    def test_admin_creation(self):
        admin = self.admin
        self.assertEqual(admin.user.name, 'TestUser')
        self.assertEqual(admin.user.role, 'Admin')
        self.assertEqual(admin.user.email, 'email@example.com')
        self.assertEqual(admin.officeNo, 'A123')

    def test_admin_update(self):
        updated_data = {
            'name': 'Updated Admin Name',
            'role': 'Updated Admin Role',
            'email': 'updated_admin@example.com',
            'address': 'Updated Admin Address',
            'officeNo': 'B456'
        }
        admin = self.admin
        admin.user.name = updated_data['name']
        admin.user.role = updated_data['role']
        admin.user.email = updated_data['email']
        admin.user.address = updated_data['address']
        admin.officeNo = updated_data['officeNo']
        admin.user.save()
        admin.save()

        admin.refresh_from_db()

        self.assertEqual(admin.user.name, updated_data['name'])
        self.assertEqual(admin.user.role, updated_data['role'])
        self.assertEqual(admin.user.email, updated_data['email'])
        self.assertEqual(admin.user.address, updated_data['address'])
        self.assertEqual(admin.officeNo, updated_data['officeNo'])

    def test_admin_deletion(self):
        admin = self.admin
        admin.user.delete()

        with self.assertRaises(Admin.DoesNotExist):
            Admin.objects.get(user__username='admin123')

    def test_event_organizer_creation(self):
        event_organizer = self.event_organizer
        self.assertEqual(event_organizer.user.name, 'TestOrganizer')
        self.assertEqual(event_organizer.user.role, 'Organizer')
        self.assertEqual(event_organizer.user.email, 'organizer@example.com')
        self.assertEqual(event_organizer.phoneNumber, '123456789')

    def test_event_creation(self):
        event = self.event
        self.assertEqual(event.name, 'Test Event')

    def test_event_update(self):
        updated_data = {
            'name': 'Updated Event Name',
            'location': 'Updated Location',
            'capacity': 200,
            'category': 'Updated Category'
        }
        event = self.event
        event.name = updated_data['name']
        event.location = updated_data['location']
        event.capacity = updated_data['capacity']
        event.category = updated_data['category']

        event.save()

        event.refresh_from_db()

        self.assertEqual(event.name, updated_data['name'])
        self.assertEqual(event.location, updated_data['location'])
        self.assertEqual(event.capacity, updated_data['capacity'])
        self.assertEqual(event.category, updated_data['category'])

    def test_event_deletion(self):
        event = self.event
        event.delete()

        with self.assertRaises(Events.DoesNotExist):
            Events.objects.get(name='Test Event')

    def test_customer_creation(self):
        customer = self.customer
        self.assertEqual(customer.user.name, 'TestCustomer')
        self.assertEqual(customer.user.role, 'Customer')
        self.assertEqual(customer.user.email, 'customer@example.com')
        self.assertEqual(customer.phoneNumber, '987654321')

    def test_event_organizer_update(self):
        updated_data = {
            'name': 'Updated Organizer Name',
            'role': 'Updated Organizer Role',
            'email': 'updated_organizer@example.com',
            'address': 'Updated Organizer Address',
            'phoneNumber': '999999999'
        }
        event_organizer = self.event_organizer
        event_organizer.user.name = updated_data['name']
        event_organizer.user.role = updated_data['role']
        event_organizer.user.email = updated_data['email']
        event_organizer.user.address = updated_data['address']
        event_organizer.phoneNumber = updated_data['phoneNumber']
        
    def test_login_page_loads(self):                       #testing for the loading of the page
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<title>Login</title>') 

    def test_login_page_status_code(self):
        # Test if the login page returns a status code of 200 (OK)
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_page_contains_title(self):
        # Test if the login page contains the expected title
        response = self.client.get(reverse('login'))
        self.assertContains(response, '<title>Login</title>')

    def test_invalid_login_credentials(self):
        # Test if the login page handles invalid credentials correctly
        username = 'invalid_user'
        password = 'invalid_password'
        response = self.client.post(reverse('login'), {'username': username, 'password': password})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<p style="color: white;">Invalid username or password.</p>')

    def test_valid_login_credentials(self):
        # Create a user with valid credentials
        username = 'mahigangal'
        password = 'mahi123'
        hashed_password = make_password(password)  # Hash the password
        user = users.objects.create(username=username, password=hashed_password)
        response = self.client.post(reverse('login'), {'username': username, 'password': password})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url=reverse('home'), target_status_code=200)

    def test_login_page_ui_elements(self):
           
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
            
            # Check if the response contains the login form elements
        self.assertContains(response, '<form')  # Check for the presence of the form
        self.assertContains(response, '<label for="username">Username</label>')  # Check for the username label
        self.assertContains(response, '<input type="text" id="username" name="username" required>')  # Check for the username input field
        self.assertContains(response, '<label for="password">Password</label>')  # Check for the password label
        self.assertContains(response, '<input type="password" id="password" name="password" required>')  # Check for the password input field
        self.assertContains(response, '<input type="submit"')  # Check for the submit button
        self.assertContains(response, '<a href="http://localhost:8000/signup/">Sign up</a>')  # Check for the signup link
        
    def test_signup_page_loads(self):                       #testing for the loading of the page
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<title>Signup Page</title>') 

    def test_signup_page_status_code(self):
        # Test if the signup page returns a status code of 200 (OK)
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_page_contains_title(self):
        # Test if the signup page contains the expected title
        response = self.client.get(reverse('signup'))
        self.assertContains(response, '<title>Signup Page</title>')


    def test_signup_page_post_success(self):
        data = {
            'username': 'divenagangal',
            'password': 'divena123',
            'name': 'Divena Gangal',
            'email': 'divenagangal@gamil.com',
            'address': '123 Test St',
            'role': 'customer'
        }
        response = self.client.post(reverse('signup'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'User Account Created for: Divena Gangal')

        # Check if the user exists in the database
        user_exists = users.objects.filter(username='divenagangal').exists()
        self.assertTrue(user_exists)

    def test_signup_page_ui_elements(self):
        
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        
        # Check if the response contains the signup form elements
        self.assertContains(response, '<form')  # Check for the presence of the form
        self.assertContains(response, '<label for="username">Username:</label>')  # Check for the username label
        self.assertContains(response, '<input type="text" id="username" name="username" required>')  # Check for the username input field
        self.assertContains(response, '<label for="password">Password:</label>')  # Check for the password label
        self.assertContains(response, '<input type="password" id="password" name="password" required>')  # Check for the password input field
        self.assertContains(response, '<label for="name">Name:</label>')  # Check for the name label
        self.assertContains(response, '<input type="text" id="name" name="name" required>')  # Check for the name input field
        self.assertContains(response, '<label for="email">Email:</label>')  # Check for the email label
        self.assertContains(response, '<input type="email" id="email" name="email" required>')  # Check for the email input field
        self.assertContains(response, '<label for="address">Address:</label>')  # Check for the address label
        self.assertContains(response, '<input type="text" id="address" name="address" required>')  # Check for the address input field
        self.assertContains(response, '<label for="role">Role:</label>')  # Check for the role label
        self.assertContains(response, '<select id="role" name="role">')  # Check for the role dropdown
        self.assertContains(response, '<option value="customer">Customer</option>')  # Check for the customer option
        self.assertContains(response, '<option value="EventOrganizer">Event Organizer</option>')  # Check for the organiser option
        self.assertContains(response, '<input type="submit"')  # Check for the submit button
        self.assertContains(response, '<a href="http://localhost:8000/login/">Login</a>')  # Check for the login link
    
    def test_add_event_page_ui_elements(self):
        response = self.client.get(reverse('add_event'))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the expected HTML elements
        self.assertContains(response, '<form')  # Check for the presence of the form
        self.assertContains(response, '<label for="name">Event Name:</label>')  # Check for the event name label
        self.assertContains(response, '<input type="text" id="name" name="name" required>')  # Check for the event name input field
        self.assertContains(response, '<label for="eventDateTime">Event Date and Time:</label>')  # Check for the event date and time label
        self.assertContains(response, '<input type="datetime-local" id="eventDateTime" name="eventDateTime" required>')  # Check for the event date and time input field
        self.assertContains(response, '<label for="location">Location:</label>')  # Check for the location label
        self.assertContains(response, '<input type="text" id="location" name="location">')  # Check for the location input field
        self.assertContains(response, '<label for="capacity">Capacity:</label>')  # Check for the capacity label
        self.assertContains(response, '<input type="number" id="capacity" name="capacity">')  # Check for the capacity input field
        self.assertContains(response, '<label for="category">Category:</label>')  # Check for the category label
        self.assertContains(response, '<input type="text" id="category" name="category">')  # Check for the category input field
        self.assertContains(response, '<label for="artist">Artist:</label>')  # Check for the artist label
        self.assertContains(response, '<input type="text" id="artist" name="artist">')  # Check for the artist input field
        self.assertContains(response, '<label for="price">Price:</label>')  # Check for the price label
        self.assertContains(response, '<input type="number" id="price" name="price" step="0.01" min="0.00" max="99999.99" required>')  # Check for the price input field
        self.assertContains(response, '<label for="image">Event Image:</label>')  # Check for the event image label
        self.assertContains(response, '<input type="file" id="image" name="image">')  # Check for the event image input field
        self.assertContains(response, '<input type="submit" value="Add Event">')  # Check for the submit button
      
    def test_add_event_with_valid_data(self):
        # Simulate a POST request with valid data
        valid_data = {
            'name': 'Test Event',
            'eventDateTime': '2024-03-30T12:00',
            'location': 'Test Location',
            'capacity': 100,
            'category': 'Test Category',
            'artist': 'Test Artist',
            'image': 'test_image.jpg'
        }
        self.client.login(username='organizer123', password='organizerpass')
        response = self.client.post(reverse('add_event'), valid_data)
        
        # Check if the event was added successfully
        self.assertEqual(response.status_code, 302)  # Redirected to home page
        self.assertTrue(Events.objects.filter(name='Test Event').exists())

