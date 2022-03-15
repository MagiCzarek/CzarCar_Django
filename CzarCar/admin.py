from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account,Rent,Car, DrivingLicense
from django.contrib.gis.db import models


admin.site.register(Rent)
admin.site.register(Car)
admin.site.register(DrivingLicense)


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username','date_joined','last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined','last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account,AccountAdmin)



