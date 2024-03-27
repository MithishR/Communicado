import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse 
from .models import *
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Example 1

class Hosttest(LiveServerTestCase):
  	
	def testhomepage(self):
		options = Options()
		options.headless = True
		driver = webdriver.Chrome(options=options)
		driver.get(self.live_server_url)
				# try driver.get(self.live_server_url) if driver.get('http://127.0.0.1:8000/') does not work	
		assert "Hello, world!" in driver.title
            
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
        role='Organizer',
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
            imageURL='test_image.jpg'
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

    


    

