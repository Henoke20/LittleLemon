from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Menu.objects.create(title="IceCream", price=10, inventory = 50)
    
    def test_get_item(self):
        item = Menu.objects.get(id=1)
        self.assertEqual(str(item),"IceCream : (\'10.00\', \'50\')")
        

            
        