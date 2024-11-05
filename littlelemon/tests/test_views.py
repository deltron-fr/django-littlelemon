from django.test import TestCase
from django.urls import reverse
from restaurant.models import Menu
from rest_framework.test import APIClient
from restaurant.serialisers import MenuSerializers

class MenuViewTest(TestCase):
    def setUp(self):
        self.item_1 = Menu.objects.create(Title="Meatpie", Price=12.00, Inventory=5)
        self.item_2 = Menu.objects.create(Title="Orange Juice", Price=10.00, Inventory=7)

        self.client = APIClient()

    def test_getall(self):
        response = self.client.get(reverse("menu"))
        menu_items = Menu.objects.all()
        serialized_data = MenuSerializers(menu_items, many=True).data

        self.assertEqual(response.data, serialized_data)
