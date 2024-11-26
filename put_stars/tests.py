from django.test import TestCase
from rest_framework.test import APIRequestFactory
from unittest.mock import patch, MagicMock
from django.contrib.auth.models import User
from .views import PutStars



class TestPutStars(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            id=1,
            username="unit_test", 
            password="password"
        )
        self.factory = APIRequestFactory()

    @patch("put_stars.views.GetRecipe")
    def test_patch(self, mock_recipe):
        recipe = MagicMock()
        data_recipe = {"id":1, "stars": 5.0}
        mock_recipe.return_value = recipe
        mock_recipe.__getitem__.return_value = recipe
        mock_recipe.recipe_filter.return_value = data_recipe
        request = self.factory.patch(
            "/put_stars/",
            data=data_recipe
        )
        view = PutStars.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 202)

