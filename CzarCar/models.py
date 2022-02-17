import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,Group

from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class AccountManager(BaseUserManager):
    def create_user(self, email, nick_name, password=None):
        if not email:
            raise ValueError("User must have an email")
        if not nick_name:
            raise ValueError("User must have nickname")
        user = self.model(
            email=self.normalize_email(email),
            nick_name=nick_name,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nick_name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            nick_name=nick_name

        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=50, unique=True)
    name = models.CharField(max_length=24)
    second_name = models.CharField(max_length=24)
    username = models.CharField(max_length=30, unique=True)
    join_date = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)




    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    object = AccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
