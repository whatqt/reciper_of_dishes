from django.test import TestCase
from rest_framework.test import APIRequestFactory
from unittest.mock import patch, MagicMock
from django.contrib.auth.models import User
from .views import PutStars
from recipes.models import Recipe
from datetime import datetime



class TestPutStars(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            id=1,
            username="unit_test", 
            password="password"
        )
        self.factory = APIRequestFactory()
        self.recipe = Recipe.objects.create(
            title="unit_test",
            ingredients="unit_test",
            instructions="unit_test",
            created_at=datetime.now(),
            stars=0.0,
            categories=["Закуски"],
            created_by_id = 1
        )


    @patch("put_stars.views.GetRecipe")
    def test_patch(self, mock_recipe):
        feedback = {"id":1, "stars": 5.0}
        recipe = MagicMock()
        mock_recipe.return_value = recipe
        recipe.__getitem__.return_value = recipe
        recipe.recipe_filter.return_value = Recipe.objects.filter(
            title="unit_test"
        )
        request = self.factory.patch(
            "/put_stars/",
            data=feedback
        )
        request.user = self.user
        view = PutStars.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 202)

