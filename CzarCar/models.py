import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group

from django.db import models
from django.core.exceptions import ValidationError
import re


# Create your models here.


class AccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("User must have an email")
        if not username:
            raise ValueError("User must have nickname")
        user = self.model(
            email=self.normalize_email(email),
            username=username,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,

        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=50, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    name = models.CharField(max_length=24)
    second_name = models.CharField(max_length=24)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    object = AccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Car(models.Model):
    STATUS = (
        ('RENTED', 'RENTED'),
        ('NOT_RENTED', 'NOT_RENTED')
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True)
    year_production = models.IntegerField(null=True)
    image = models.ImageField(upload_to='uploads/', null=True)
    description = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.name


class Rent(models.Model):
    account = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL)
    car = models.ForeignKey(Car, null=True, on_delete=models.SET_NULL)
    car.status = 'RENTED'
    delivery_adress = models.CharField(max_length=200)
    rent_price = models.FloatField(null=True)
    rent_time = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.id)

    def calculate_price(self):
        self.rent_price = self.car.price * self.rent_time


class DrivingLicense(models.Model):
    name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    license_number = models.CharField(max_length=8, unique=True, null=False)
    account = models.OneToOneField(Account, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.license_number
