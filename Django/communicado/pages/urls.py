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
    path("organizer_actions",views.organizer_actions , name = 'organizer_actions'),
    path('add_event', views.add_event, name='add_event'),
    path('edit_event', views.edit_event, name='edit_event'),
    path('change_event/<int:event_ID>/', views.change_event, name='change_event'),
    path('userbookinfo',views.userbookeventinfo , name = 'userbookeventinfo'),
    path('add_to_cart/<int:event_ID>/', views.add_to_cart, name='add_to_cart'),
    path('payment', views.payment, name='payment'),
    path('admin_actions', views.admin_actions, name='admin_actions'),
    path('pending', views.pending, name='pending'),
    path('rejected', views.rejected, name='rejected'),

 
]
