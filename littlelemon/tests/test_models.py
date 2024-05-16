from django.test import TestCase
from restaurant.models import MenuItem
from decimal import Decimal

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(
            title="Cheeseburger",
            price=Decimal("7.50"),
            inventory=100,
        )
        self.assertEqual(str(item), "Cheeseburger : 7.50")
