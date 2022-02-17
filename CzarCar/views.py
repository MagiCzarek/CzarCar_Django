from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout

from .decorators import unauthenticated_user, admin_only
from .models import Question, Choice
from CzarCar.forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import admin


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
