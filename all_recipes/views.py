from rest_framework import status
from django.shortcuts import redirect
from rest_framework.views import Response
from rest_framework.views import APIView, Request
from .serializer import AllViewRecipeSerializer
from django.contrib.auth.models import User
from create_recipes.models import Recipe
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers


class AllRecipes(APIView):
    def get_queryset(self):
        recipes = Recipe.objects.all().values()
        return recipes

    def get(self, request: Request):
        data_recipes = self.get_queryset()
        # print(data_recipes)
        ready_recipes = []
        for data_recipe in data_recipes:
            dict_data_recipe = dict(data_recipe)
            del dict_data_recipe["id"]
            del dict_data_recipe['created_by_id']
            dict_data_recipe['created_by'] = request.user.pk
            # print(dict_data_recipe)
            serializer = AllViewRecipeSerializer(data=dict_data_recipe)
            print(serializer.is_valid())
            if serializer.is_valid():
                serializer.validated_data['created_by'] = request.user.username
                print(serializer.validated_data)
                ready_recipes.append(serializer.validated_data)
            else: return Response(serializer.errors)
        return Response({"recipes": ready_recipes})

