# Generated by Django 3.2.5 on 2022-01-25 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CzarCar', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='nick_name',
            new_name='username',
        ),
    ]