from rest_framework import status
from django.shortcuts import redirect
from rest_framework.views import Response
from rest_framework.views import APIView, Request
from .serializer import MyRecipeUpdateSerializer
from django.contrib.auth.models import User
from create_recipes.models import Recipe
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers


class UpdateMyRecipe(APIView):
    def get_queryset(self):
        try:
            return Recipe.objects.filter(created_by=self.request.user)
        except ObjectDoesNotExist:
            return None
    
    def get(self, request: Request, title):
        data_recipe = self.get_queryset().get(title=title)
        if data_recipe:
            serializer = MyRecipeUpdateSerializer(
                {
                    "title": data_recipe.title,
                    "ingredients": data_recipe.ingredients,
                    "instructions": data_recipe.instructions,
                    "categories": data_recipe.categories,
                    'created_by': data_recipe.created_by
                }
            )
            return Response(serializer.data)

    def patch(self, request: Request, title):
        data_recipe = self.get_queryset()
        if data_recipe:
            recipe_instance = data_recipe.get(title=title)
            serializer = MyRecipeUpdateSerializer(recipe_instance, data=request.data , partial=True)
            print(serializer.is_valid())
            print(data_recipe.filter(title=title).get(title=title))
            print(serializer.validated_data)
            if serializer.is_valid():
                serializer.update(data_recipe.get(title=title), serializer.validated_data)
                return Response({"Recipe": "Update"})
            else: return Response(serializer.errors)


{"title": "testtttt", "ingredients": "test", "instructions": "test", "categories":["Закуски"]}
{"new_title":"testt1tfasd","title": "testtttt", "ingredients": "test", "instructions": "test", "categories":["Закуски"]}
