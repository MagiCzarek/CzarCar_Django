from django.http import HttpResponse
from django.shortcuts import redirect, render

from CzarCar.models import DrivingLicense


def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)

    return wrapper_func

# def allowed_roles(is_admin,is_client):
#     def decorator(view_func):
#             def wrapper_func(request,*args,**kwargs):
#
#
#                 return view_func(request, *args, **kwargs)
#             return wrapper_func
#     return decorator()
def logged_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('home')

    return wrapper_func

def admin_only(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_admin:
            return view_func(request,*args,**kwargs)
        else:
            return redirect('user-page')

    return wrapper_func

# def driving_license(view_func):
#     def wrapper_func(request,*args,**kwargs):
#         user = request.user
#         driving_licenses = DrivingLicense.objects.filter(account=user)
#         if driving_licenses is None:
#             return view_func(request, *args, **kwargs)
#
#         else:
#             context = {'driving_licenses': driving_licenses}
#             return render(request, 'CzarCar/profile.html', context)
#
#     return wrapper_func