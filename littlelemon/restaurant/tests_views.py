from django.test import TestCase
from .models import *
# Create your tests here.
class BookingViewTest(TestCase):
    def test_if_work(self):
        item = str(Booking.objects.create(name='jeff',no_of_guests=5,booking_date='2023-10-23'))
        print(Booking.objects.all())
        print(item)
        self.assertEqual(item,"jeff : 2023-10-23")