from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from json import dumps
from .views import Recipes
from unittest.mock import patch, MagicMock
from django.db.models.query import QuerySet
from recipes.models import Recipe
from datetime import datetime



class TestRecipes(TestCase):
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
    
    @patch("recipes.views.GetRecipe")
    def test_get_id(
            self, mock_get_recipe
        ):
        recipe = {
            "title": "testtttt",
            "ingredients": "test",
            "instructions": "test",
            "stars": "0.0",
            "categories": [
                "Закуски"
            ],
            "created_by_id": 1
        }
        get_recipe = MagicMock()
        mock_get_recipe.return_value = get_recipe
        get_recipe.__getitem__.return_value = get_recipe
        get_recipe.recipe_filter.return_value = recipe
        get_recipe.recipe_values.return_value = recipe
        request = self.factory.get(
            '/recipe/1', 
        )
    
        request.user = self.user
        view = Recipes.as_view()
        response = view(request, id_recipe = 1)
        self.assertEqual(response.status_code, 302)

    @patch("recipes.views.IterationRecipesAtId")
    def test_get_not_id(
        self, mock_iteration_recipes
        ):
        iteration_recipes = MagicMock()
        mock_iteration_recipes.return_value = iteration_recipes
        iteration_recipes.__getitem__.return_value = iteration_recipes
        iteration_recipes.iteration.return_value = {
            "id": 36,
            "title": "unit_test",
            "ingredients": "unit_test",
            "instructions": "unit_test",
            "created_at": "2024-11-24T19:13:57.905176Z",
            "stars": 0.0,
            "categories": [
                "Закуски"
            ],
            "created_by": 1
        }
        request = self.factory.get('/recipe/')
        request.user = self.user
        view = Recipes.as_view()
        response = view(request, id_recipe=0)
        self.assertEqual(response.status_code, 302)

    def test_post(self):
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
        view = Recipes.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 201)

    @patch("recipes.views.RightsToDeleteOrPatchOrGet")
    def test_delete(self, mock_rights_to_delete):
        rights_to_delete = MagicMock()
        mock_rights_to_delete.return_value = rights_to_delete
        rights_to_delete.__getitem__.return_value = rights_to_delete
        rights_to_delete.chek.return_value = self.recipe
        request = self.factory.delete('/recipe/1')
        request.user = self.user
        view = Recipes.as_view()
        response = view(request, id_recipe=1)
        self.assertEqual(response.status_code, 202)

    @patch("recipes.views.RightsToDeleteOrPatchOrGet")
    def test_patch(self, mock_rights_to_update):
        data_recipe = {
            "title": "test", 
            "ingredients": "test", 
            "instructions": "test", 
            "categories":["Закуски"]
        }
        rights_to_update = MagicMock()
        mock_rights_to_update.return_value = rights_to_update
        rights_to_update.__getitem__.return_value = rights_to_update
        rights_to_update.chek.return_value = self.recipe
        request = self.factory.patch(
            '/recipe/1',
            data=data_recipe
        )
        request.user = self.user
        view = Recipes.as_view()
        response = view(request, id_recipe=1)
        self.assertEqual(response.status_code, 202)

