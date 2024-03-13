# models.py

from django.db import models
from django.contrib.auth.models import User

class users(models.Model):
    userID = models.AutoField(primary_key=True)
    role = models.CharField(max_length=50)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username

class events(models.Model):
    eventID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    eventDateTime = models.DateTimeField()
    location = models.CharField(max_length=100, blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    artist = models.CharField(max_length=100, blank=True, null=True)
    isVerified = models.BooleanField(default=False)
    adminID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_events', blank=True, null=True)
    eventOrganizerID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organizer_events', blank=True, null=True)

    class Meta: 
        db_table = 'events'

    def __str__(self):
        return self.name

class EventOrganizer(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=30)

    class Meta: 
        db_table = 'EventOrganizer'

    def __str__(self):
        return f"{self.user.username} ({self.phoneNumber})"

class Customer(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=30)

    class Meta:
        db_table = 'Customer'

    def __str__(self):
        return f"{self.user.username} ({self.phoneNumber})"

class BookedEvent(models.Model):
    eventID = models.OneToOneField(events, primary_key=True, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    isPaid = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    referenceNumber = models.CharField(max_length=40)

    class Meta:
        db_table = 'bookedEvent'

    def __str__(self):
        return f"{self.eventID.name} - {self.referenceNumber}"
