from rest_framework import status
from django.shortcuts import redirect
from rest_framework.views import Response
from rest_framework.views import APIView, Request
from .serializer import AllViewRecipeSerializer
from django.contrib.auth.models import User
from recipes.models import Recipe
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers


class AllRecipes(APIView):
    def get_queryset(self):
        recipes = Recipe.objects.all().values()
        return recipes

    def get(self, request: Request):
        data_recipes = self.get_queryset()
        page_number = request.query_params.get('page_number', 1)
        len_data_recipes = len(data_recipes)
        validated_recipes = []
        dict_recipes = {}
        quantity_add_recipe = 0
        select_page = 1
        for data_recipe in data_recipes:
            dict_data_recipe = dict(data_recipe)
            del dict_data_recipe["id"]
            user = User.objects.get(id=dict_data_recipe['created_by_id'])
            dict_data_recipe['created_by'] = user.pk
            # print(dict_data_recipe)
            serializer = AllViewRecipeSerializer(data=dict_data_recipe)
            print(serializer.is_valid())
            if serializer.is_valid():
                serializer.validated_data['created_by'] = user.username
                print(serializer.validated_data)
                validated_recipes.append(serializer.validated_data)
                quantity_add_recipe+=1
                match quantity_add_recipe:
                    case 5:
                        print("5 записей")
                        dict_recipes[select_page] = validated_recipes.copy()
                        select_page +=1
                        validated_recipes.clear()
                        quantity_add_recipe = 0

            else: return Response(serializer.errors)


        if quantity_add_recipe != 0:
            dict_recipes[select_page] = validated_recipes.copy()
        
        if len_data_recipes < 5:
            print(dict_recipes)
            return Response({"recipes": validated_recipes})
        else: return Response({"recipes": dict_recipes[int(page_number)]})

# доработать, поскольку выбор следующей страницы всё равно будет грузить лишнее данные.
# изначальная задумка в том, что все данные подгружаются тогда, когда пользователь переходит на новую странциу.
