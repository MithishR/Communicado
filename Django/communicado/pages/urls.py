from django.urls import path
from pages import views

urlpatterns = [
    path("", views.home, name='home'),
    path("login/",views.login , name = 'login'),
    path("signup/", views.signup , name ='signup'),
    path("useracc", views.useracc, name='useracc'),
    path("events",views.event , name = 'events'),
    path('eventinfo/<int:event_ID>', views.eventinfo, name='eventinfo'),
    path("xyz",views.xyz , name = 'xyz'),
 
]