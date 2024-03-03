from django.test import TestCase
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer, BookingSerializer
from django.urls import reverse

class MenuViewTest(TestCase):
    @classmethod
    def setUp(cls):
        foods = ['Hamburger','Cheeseburger','Pasta','Chicken Sandwich','Taco']
        
        for i in range(5):
            Menu.objects.create(title=foods[i], price=10.00 + i, inventory = (i+1)*10)
    
    def test_getall(self):
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        #print(list(serializer.data))
        expected_data = [
            {'id':2, 'title': 'Hamburger', 'price': '10.00', 'inventory': 10},
            {'id':3, 'title': 'Cheeseburger', 'price': '11.00', 'inventory': 20},
            {'id':4, 'title': 'Pasta', 'price': '12.00', 'inventory': 30},
            {'id':5, 'title': 'Chicken Sandwich', 'price': '13.00', 'inventory': 40},
            {'id':6, 'title': 'Taco', 'price': '14.00', 'inventory': 50}
             
        ]
        self.assertEqual(serializer.data, expected_data)
