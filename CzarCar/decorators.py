from django.http import HttpResponse
from django.shortcuts import redirect

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


def admin_only(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_admin:
            return view_func(request,*args,**kwargs)
        else:
            return redirect('user-page')

    return wrapper_func