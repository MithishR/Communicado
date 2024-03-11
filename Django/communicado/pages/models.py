from django.db import models

# Create your models here.
class users(models.Model):
    userID = models.AutoField(primary_key=True)
    role = models.CharField(max_length=50)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'users'
class events(models.Model):
    eventID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    eventDateTime = models.DateTimeField()
    location = models.CharField(max_length=100, blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    artist = models.CharField(max_length=100, blank=True, null=True)
    isVerified = models.BooleanField(default=False)
    #admin = models.ForeignKey(users, on_delete=models.CASCADE, related_name='admin_events', blank=True, null=True)
    #eventOrganizer = models.ForeignKey(users, on_delete=models.CASCADE, related_name='organizer_events', blank=True, null=True)
    class Meta:
        db_table = 'events'