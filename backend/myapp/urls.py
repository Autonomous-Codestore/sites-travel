from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('group', views.group_trips, name='group_trips'),
    path('group/<int:pk>', views.group_trip, name='group_trip'),

    path('custom', views.custom_trips, name='custom'),

    path('flight_list', views.flight_list, name='flight_list'),
    path('flight_detail/<str:pk>', views.flight_detail, name='flight_detail'),

    path('car_list', views.car_list, name='car_list'),
    path('car_detail/<str:pk>', views.car_detail, name='car_detail'),

    path('gallery', views.gallery, name='gallery'),   
    path('contacts', views.contacts, name='contacts'),

    path('main', views.main, name='main'),
    path('trips', views.trips, name='trips'),
    path('trip/<str:pk>', views.trip, name='trip'),

    path('flights', views.flights, name='flights'),
    path('flight/<str:pk>', views.flight, name='flight'),

    path('cars', views.cars, name='cars'),
    path('car/<str:pk>', views.car, name='car'),

    path('bookings', views.bookings, name='bookings'),
    path('booking/<str:pk>', views.booking, name='booking'),

    path('drivers', views.drivers, name='drivers'),

    path('trip_availability/<str:pk>', views.trip_availability, name='trip_availability'),
    path('flight_availability//<str:pk>', views.flight_availability, name='flight_availability'),
    path('car_availability/<str:pk>', views.car_availability, name='car_availability'),            


    path('step', views.step, name='step'),
    path('stepsave', views.stepsave, name='stepsave'),


]
