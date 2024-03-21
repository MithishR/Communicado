from django.test import TestCase
from .models import *  

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
    def test_event_organizer_creation(self):
        event_organizer = self.event_organizer
        self.assertEqual(event_organizer.user.name, 'TestOrganizer')
        self.assertEqual(event_organizer.user.role, 'Organizer')
        self.assertEqual(event_organizer.user.email, 'organizer@example.com')
        self.assertEqual(event_organizer.phoneNumber, '123456789')

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
        event_organizer.user.save()
        event_organizer.save()

        event_organizer.refresh_from_db()

        self.assertEqual(event_organizer.user.name, updated_data['name'])
        self.assertEqual(event_organizer.user.role, updated_data['role'])
        self.assertEqual(event_organizer.user.email, updated_data['email'])
        self.assertEqual(event_organizer.user.address, updated_data['address'])
        self.assertEqual(event_organizer.phoneNumber, updated_data['phoneNumber'])

    def test_customer_update(self):
        updated_data = {
            'name': 'Updated Customer Name',
            'role': 'Updated Customer Role',
            'email': 'updated_customer@example.com',
            'address': 'Updated Customer Address',
            'phoneNumber': '888888888'
        }
        customer = self.customer
        customer.user.name = updated_data['name']
        customer.user.role = updated_data['role']
        customer.user.email = updated_data['email']
        customer.user.address = updated_data['address']
        customer.phoneNumber = updated_data['phoneNumber']
        customer.user.save()
        customer.save()

        customer.refresh_from_db()

        self.assertEqual(customer.user.name, updated_data['name'])
        self.assertEqual(customer.user.role, updated_data['role'])
        self.assertEqual(customer.user.email, updated_data['email'])
        self.assertEqual(customer.user.address, updated_data['address'])
        self.assertEqual(customer.phoneNumber, updated_data['phoneNumber'])

    def test_event_organizer_deletion(self):
        event_organizer = self.event_organizer
        event_organizer.user.delete()

        with self.assertRaises(EventOrganizer.DoesNotExist):
            EventOrganizer.objects.get(user__username='testorganizer123')

    def test_customer_deletion(self):
        customer = self.customer
        customer.user.delete()

        with self.assertRaises(Customer.DoesNotExist):
            Customer.objects.get(user__username='testcustomer123')
