from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.contrib.auth.models import User
from unittest.mock import patch, MagicMock
from .views import MyRecipe
from datetime import datetime
from recipes.models import Recipe


class TestMyRecipe(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            id=1,
            username="unit_test", 
            password="password"
        )
        self.recipe = Recipe.objects.create(
            title="unit_test",
            ingredients="unit_test",
            instructions="unit_test",
            created_at=datetime.now(),
            stars=0.0,
            categories=["Закуски"],
            created_by_id = 1
        )

    @patch("my_recipes.views.RightsToDeleteOrPatchOrGet")
    def test_get_id(
        self, mock_rights_get
    ):  
        recipe = MagicMock()
        data_recipe = {
            "title": "testtt",
            "ingredients": "test",
            "instructions": "test",
            "stars": "4.0",
            "categories": [
                "Закуски"
            ]
        }
        mock_rights_get.return_value = recipe
        recipe.__getitem__.return_value = recipe
        recipe.chek.return_value = data_recipe
        recipe.recipe_get.return_value = self.recipe
        request = self.factory.get(
            "/my_recipe/1"
        )
        request.user = self.user
        view = MyRecipe.as_view()
        response = view(request, id_recipe=1)
        self.assertEqual(response.status_code, 302)

    @patch("my_recipes.views.IterationRecipes")
    @patch("my_recipes.views.GetMyRecipes")
    def test_get_not_id(
        self, mock_recipes, mock_iteration_recipes
    ):
        data_recipes = [
            {
                "title": "testtt",
                "ingredients": "test",
                "instructions": "test",
                "stars": "4.0",
                "categories": [
                    "Закуски"
                ]
            }
        ]
        recipes = MagicMock()
        mock_recipes.return_value = recipes
        recipes.__getitem__.return_value = recipes
        recipes.get_recipes.return_value = data_recipes

        iteration_recipes = MagicMock()
        mock_iteration_recipes.return_value = iteration_recipes
        iteration_recipes.__getitem__.return_value = iteration_recipes
        iteration_recipes.iteration.return_value = data_recipes
        request = self.factory.get("/my_recipe/")
        request.user = self.user
        view = MyRecipe.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 302)
