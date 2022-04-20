from django.test import SimpleTestCase
from django.urls import reverse, resolve

from CzarCar.views import *


class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEqual(resolve(url).func, home_view)

    def test_registration_url_is_resolved(self):
        url = reverse('CzarCar:registration')
        print(resolve(url))
        self.assertEqual(resolve(url).func, registration_view)

    def test_login_url_is_resolved(self):
        url = reverse('CzarCar:login')
        print(resolve(url))
        self.assertEqual(resolve(url).func, login_view)

    def test_contact_url_is_resolved(self):
        url = reverse('CzarCar:contact')
        print(resolve(url))
        self.assertEqual(resolve(url).func, contact_view)

    def test_about_url_is_resolved(self):
        url = reverse('CzarCar:about')
        print(resolve(url))
        self.assertEqual(resolve(url).func, about_view)

    def test_rent_url_is_resolved(self):
        url = reverse('CzarCar:rent')
        print(resolve(url))
        self.assertEqual(resolve(url).func, car_view)

    def test_map_url_is_resolved(self):
        url = reverse('CzarCar:map')
        print(resolve(url))
        self.assertEqual(resolve(url).func, map_view)

    def test_rented_cars_url_is_resolved(self):
        url = reverse('CzarCar:rented_cars')
        print(resolve(url))
        self.assertEqual(resolve(url).func, your_rent_view)

    def test_payment_url_is_resolved(self):
        url = reverse('CzarCar:payment')
        print(resolve(url))
        self.assertEqual(resolve(url).func, payment_view)
