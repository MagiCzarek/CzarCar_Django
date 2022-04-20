from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout

from .decorators import unauthenticated_user, admin_only, logged_user

from CzarCar.forms import RegistrationForm, EditDrivingLicenseForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from .models import *


# Create your views here.

# @login_required(login_url='login')
def home_view(request):
    if request.user.is_authenticated:
        request.user = f'You are logged as {request.user}'
    else:
        request.user = f'Not logged in'
    print(request.headers)
    return render(request, 'home.html', {})


@unauthenticated_user
def registration_view(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created for: ' + user)

            return redirect('home')
    context = {'form': form}
    return render(request, 'CzarCar/registration.html', context)


@unauthenticated_user
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or pass incorrect')
    context = {}
    return render(request, 'CzarCar/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def contact_view(request):
    print(request.headers)
    return render(request, 'CzarCar/contact.html', {})


def about_view(request):
    print(request.headers)
    return render(request, 'CzarCar/about.html', {})


def car_view(request):
    # cars = Car.objects.filter(status='NOT_RENTED')
    if request.method == 'POST' and "rent" in request.POST:
        car_id = request.POST.get('car_id')
        cars = Car.objects.filter(id=car_id)
        context = {'cars': cars}
        return payment_view(request, context)
    else:
        cars = Car.objects.all()
        context = {'cars': cars}
        return render(request, 'CzarCar/rent.html', context)


@logged_user
def payment_view(request, cars):
    user = request.user

    driving_licenses = DrivingLicense.objects.filter(account=user)
    driving_licenses_count = driving_licenses.count()
    # print(driving_licenses_count)
    print(cars)

    if driving_licenses_count > 0:

        if request.method == 'POST' and "rent_car" in request.POST:
            print("git")
            rent_time = request.POST.get('rent_time')
            adress = request.POST.get('address')
            print(rent_time)
            car = Car.objects.filter(id=request.POST.get('car_id'))
            rent = Rent.objects.create(account=user, car=car, rent_time=rent_time, delivery_adress=adress)
            rent.calculate_price()
            return redirect('home')

        return render(request, 'CzarCar/payment.html', cars)
    else:

        messages.info(request, 'You need to add driving license')
        return redirect('home')


def map_view(request):
    print(request.headers)
    return render(request, 'CzarCar/map.html', {})


@logged_user
def profile_view(request):
    user = request.user
    driving_licenses = DrivingLicense.objects.filter(account=user)
    driving_licenses_count = driving_licenses.count()

    if driving_licenses_count == 0:

        if request.method == 'POST':
            name = request.POST.get('name')
            second_name = request.POST.get('secondname')
            license_number = request.POST.get('license_number')
            driving_license = DrivingLicense.objects.create(name=name, second_name=second_name,
                                                            license_number=license_number, account=user)


            return redirect('home')
        # else:
        #     messages.info(request, 'Something went wrong')

        # else:

        context = {}
        return render(request, 'CzarCar/edit_profile.html', context)
    else:

        context = {'driving_licenses': driving_licenses}
        return render(request, 'CzarCar/profile.html', context)


@logged_user
def your_rent_view(request):
    # print(request.headers)
    user = request.user
    rents = Rent.objects.filter(account=user)
    context = {'rents': rents}

    return render(request, 'CzarCar/rented_cars.html', context)
