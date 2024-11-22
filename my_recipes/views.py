from rest_framework import status
from django.shortcuts import redirect
from rest_framework.views import Response
from rest_framework.views import APIView, Request
from .serializer import GetRecipeSerializer, GetRecipesSerializer
from django.contrib.auth.models import User
from recipes.models import Recipe
from django.core.exceptions import ObjectDoesNotExist



class MyRecipe(APIView):
    def get_queryset(self, title):
        try:
            return Recipe.objects.filter(created_by=self.request.user).get(title=title)
        except ObjectDoesNotExist:
            return None

    def get(self, request: Request, title):
        data_recipe = self.get_queryset(title)
        if data_recipe:
            serializer = GetRecipeSerializer(
                data={
                    "title": data_recipe.title,
                    "ingredients": data_recipe.ingredients,
                    "instructions": data_recipe.instructions,
                    "created_at": data_recipe.created_at,
                    "start": data_recipe.starts,
                    "categories": data_recipe.categories
                }
            )
            print(serializer.is_valid())
            if serializer.is_valid():
                return Response({"data_recipe": serializer.data}) 
            
        return Response({"data_recipe": data_recipe})
       
class MyRecipes(APIView):
    def get_queryset(self):
        try:
            return Recipe.objects.filter(created_by=self.request.user).values_list("title", flat=True)
        except ObjectDoesNotExist:
            return None

    def get(self, request: Request):
        recipes = self.get_queryset()
        recipes_validated = []
        print(recipes)
        if recipes:
            for recipe in recipes:
                serializer = GetRecipesSerializer(data={"title": recipe})
                print(serializer.is_valid())
                if serializer.is_valid():
                    recipes_validated.append(recipe)
                    print(recipes_validated)
                else: return Response(serializer.errors)

            return Response({"Your recipes": recipes_validated})
        
        return Response({"Your recipes": None})
                    


# сделать еще фильтрацию, а именно поиск по рейтингу, по дате создания, по названию (в афлавитном порядке)