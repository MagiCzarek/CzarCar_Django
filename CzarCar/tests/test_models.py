from django.test import TestCase
from CzarCar.models import *


class TestModels(TestCase):
    def setUp(self):
        self.car1 = Car.objects.create(
            name='Car 1 ',
            price =200,
            category='sport',
            year_production='1997',
            image='null',
            description='hey hey',
            status='RENTED'
        )
        self.rent1 = Rent.objects.create(
            car=self.car1,
            rent_time=20
        )
    def test_rent_calculate_price(self):
        self.rent1.calculate_price()
        self.assertEqual(self.rent1.rent_price,4000)