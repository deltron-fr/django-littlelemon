from django.test import TestCase


class MenuTest(TestCase):
    def test_get_item(self):
        from restaurant.models import Menu
        item = Menu.objects.create(Title="Meatpie", Price=12.00, Inventory=5)
        self.assertEqual(str(item), "Meatpie : 12.0")