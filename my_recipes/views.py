from rest_framework import status
from django.shortcuts import redirect
from rest_framework.views import Response
from rest_framework.views import APIView, Request
from .serializer import GetRecipeSerializer
from django.contrib.auth.models import User
from create_recipes.models import Recipe
from django.core.exceptions import ObjectDoesNotExist



class MyRecipes(APIView):
    def get_queryset(self, title):
        try:
            return Recipe.objects.filter(created_by=self.request.user).get(title=title)
        except ObjectDoesNotExist:
            return None

    def get(self, request: Request, title):
        data_recipe = self.get_queryset(title)
        if data_recipe:
            serializer = GetRecipeSerializer(
                {
                    "title": data_recipe.title,
                    "ingredients": data_recipe.ingredients,
                    "instructions": data_recipe.instructions,
                    "created_at": data_recipe.created_at,
                }
            )
            return Response({"data_recipe": serializer.data})
        else: return Response({"data_recipe": "None"})
