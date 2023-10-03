from django.test import TestCase
from .models import *

# Create your tests here.
class MenuTest(TestCase):
    def test_get_item(self):
        item = str(Menu.objects.create(title='Ice Cream',price=5,inventory=100))
        print(item)
        self.assertEqual(item,"Ice Cream : 5")