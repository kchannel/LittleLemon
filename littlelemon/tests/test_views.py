from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
import json

class MenuViewTest(TestCase):
    def setUp(self):
        # Add some test instances of the Menu model
        MenuItem.objects.create(title="Cheeseburger", price=7.50, inventory=100)

    def test_get_all(self):
        # Create an API client
        client = APIClient()

        # Send a GET request to the menu endpoint
        response = client.get('/restaurant/menu/')

        # Retrieve all the Menu objects
        menus = MenuItem.objects.all()

        # Serialize the Menu objects
        serializer = MenuItemSerializer(menus, many=True)

        # Assert that the serialized data matches the response data
        self.assertEqual(json.loads(response.content), serializer.data)
