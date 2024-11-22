from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from json import dumps
from .views import Recipe



class TestCreateRecipes(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="unit_test", 
            password="password"
        )
        self.factory = APIRequestFactory()

    def test_create_recipe_post(self):
        data = {
            "title": "test", 
            "ingredients": "test", 
            "instructions": "test", 
            "categories":["Закуски"]
        }
        request = self.factory.post(
            "create_recipe/",
            dumps(data),          
            content_type='application/json'
        )
        request.user = self.user
        view = Recipe.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 201)


# Create your tests here.
