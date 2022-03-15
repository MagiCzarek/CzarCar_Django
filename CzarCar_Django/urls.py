"""CzarCar_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from CzarCar.views import home_view, contact_view, about_view, car_view, map_view, profile_view, your_rent_view, \
    payment_view

from CzarCar.views import registration_view, login_view, logout_view

urlpatterns = [

    path('', home_view, name='home'),
    path('CzarCar/', include('CzarCar.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('register/', registration_view, name='registration'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('rent/', car_view, name='rent'),
    path('map/', map_view, name='map'),
    path('profile/', profile_view, name='profile'),
    path('rented_cars.html/', your_rent_view, name='rented_cars'),
    path('payment.html/', payment_view, name='payment'),

]

urlpatterns += staticfiles_urlpatterns()
