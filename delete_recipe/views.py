from rest_framework import status
from django.shortcuts import redirect
from rest_framework.views import Response
from rest_framework.views import APIView, Request
from .serializer import DeleteRecipeSerializer
from django.contrib.auth.models import User
from create_recipes.models import Recipe
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers


class DeleteRecipe(APIView):
    def get_queryset(self, title):
        try:
            recipe = Recipe.objects.filter(created_by_id=self.request.user).get(title=title)
            return recipe
        except ObjectDoesNotExist:
            return None

    def delete(self, request: Request, title: str):
        data_recipe = self.get_queryset(title)
        if data_recipe:
            serializer = DeleteRecipeSerializer(data={"title": title})
            print(serializer.is_valid())
            if serializer.is_valid():
                data_recipe.delete()
                return Response({"Recipe delete": "completed successfully"})
            return Response(serializer.errors)
        else: return Response({"Recipe delete": "Recipe is not delete"})