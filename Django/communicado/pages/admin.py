# admin.py

from django.contrib import admin
from .models import *

class UsersAdmin(admin.ModelAdmin):
    list_display = ('userID', 'role', 'username', 'email', 'address')
    search_fields = ('username', 'email')

class EventsAdmin(admin.ModelAdmin):
    list_display = ('eventID', 'name', 'eventDateTime', 'location', 'capacity', 'category', 'artist', 'isVerified', 'adminID', 'eventOrganizerID')
    search_fields = ('name', 'category', 'artist')
    list_filter = ('isVerified',)

class EventOrganizerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phoneNumber')
    search_fields = ('user__username', 'phoneNumber')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phoneNumber')
    search_fields = ('user__username', 'phoneNumber')

class BookedEventAdmin(admin.ModelAdmin):
    list_display = ('eventID', 'quantity', 'isPaid', 'user', 'referenceNumber')
    search_fields = ('eventID__name', 'referenceNumber')
    list_filter = ('isPaid',)

admin.site.register(users, UsersAdmin)
admin.site.register(Events, EventsAdmin)
admin.site.register(EventOrganizer, EventOrganizerAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(BookedEvent, BookedEventAdmin)
