from django.test import TestCase
from restaurant.models import MenuItem, Booking

class MenuItemTest(TestCase):
    def test_get_item_01(self):
        item = MenuItem.objects.create(title_menu="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "Icream: 80")

    def test_get_item_02(self):
        item = MenuItem.objects.create(title_menu="lemon", price=3.0, inventory=5)
        self.assertEqual(str(item), "lemon: 3.0")
    
    def test_get_item_03(self):
        item = MenuItem.objects.create(title_menu="lemon", price=3.0, inventory=7)
        self.assertEqual(str(item), "lemon: 3.0")

    def test_get_item_04(self):
        item = MenuItem.objects.create(title_menu="salad", price=5.0, inventory=12)
        self.assertEqual(str(item), "salad: 5.0")

