from django.db import models

class users(models.Model):
    userID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username
class EventOrganizerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user__role__in=['Event Organizer', 'organiser', 'EventOrganizer'])

class EventOrganizer(models.Model):
    user = models.OneToOneField(users, primary_key=True, db_column='userID',on_delete=models.CASCADE, to_field='userID')
    phoneNumber = models.CharField(max_length=30)
    objects = EventOrganizerManager()

    class Meta:
        db_table = 'EventOrganizer'

    def __str__(self):
        return f"{self.user.username} ({self.phoneNumber})"
    

class Customer(models.Model):
    user = models.OneToOneField(users, primary_key=True,  db_column='userID',on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=30)

    class Meta:
        db_table = 'Customer'

    def __str__(self):
        return f"{self.user.username} ({self.phoneNumber})"

class Admin(models.Model):
    user = models.OneToOneField(users, primary_key=True, db_column='userID', on_delete=models.CASCADE)
    officeNo = models.CharField(max_length=30)
   
    class Meta:
        db_table = 'Admin'

    def __str__(self):
        return f"{self.user.username} ({self.officeNo})"

class Events(models.Model):
    eventID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    eventDateTime = models.DateTimeField()
    location = models.CharField(max_length=100, null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    artist = models.CharField(max_length=100, null=True, blank=True)
    isVerified = models.BooleanField(default=False)
    adminID = models.ForeignKey(Admin, on_delete=models.CASCADE, null=True, blank=True,db_column= "adminID")
    eventOrganizerID = models.ForeignKey(EventOrganizer, on_delete=models.CASCADE, null=True, blank=True,db_column="eventOrganizerID")
    imageURL = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True) 
    # isPendingApproval = models.BooleanField(default=True)
    

    class Meta:
        db_table = 'events'

    def __str__(self):
        return self.name

class BookedEvent(models.Model):
    eventID = models.OneToOneField(Events, primary_key=True, db_column='userID',on_delete=models.CASCADE)
    quantity = models.IntegerField()
    isPaid = models.BooleanField()
    user = models.ForeignKey(users, on_delete=models.CASCADE)
    referenceNumber = models.CharField(max_length=40)

    class Meta:
        db_table = 'bookedEvent'

    def __str__(self):
        return f"{self.eventID.name} - {self.referenceNumber}"
