from django.urls import path
from . import views

from CzarCar.views import *
app_name = 'CzarCar'
urlpatterns = [
    path('register/', registration_view, name='registration'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('rent/', car_view, name='rent'),
    path('map/', map_view, name='map'),
    path('profile/', profile_view, name='profile'),
    path('rented_cars/', your_rent_view, name='rented_cars'),
    path('payment/', payment_view, name='payment'),
]
