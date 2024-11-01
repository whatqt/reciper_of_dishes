from rest_framework import status
from django.shortcuts import redirect
from rest_framework.views import Response
from rest_framework.views import APIView, Request
from .serializer import SearchRecipeSerializer
from django.contrib.auth.models import User
from create_recipes.models import Recipe
from django.core.exceptions import ObjectDoesNotExist



class SearchRecipeForTitle(APIView):
    def get_quaryset(self, title):
        try:
            recipe = Recipe.objects.filter(title=title)
            return recipe
        except ObjectDoesNotExist: 
            return None
        
    def get(self, request: Request):
        title = request.query_params.get("title")
        recipes = self.get_quaryset(title)
        validated_recipes = []
        if recipes:
            data_recipes = recipes.values('title', 'ingredients', 'created_by')
            print(data_recipes)
            for recipe in data_recipes:
                user = User.objects.get(id=recipe['created_by'])
                recipe['created_by'] = user.pk
                print(recipe)
                serializer = SearchRecipeSerializer(data=dict(recipe))
                print(serializer.is_valid())
                if serializer.is_valid():
                    print(serializer.validated_data)
                    serializer.validated_data['created_by'] = user.username
                    validated_recipes.append(serializer.validated_data)
                else: return Response(serializer.errors)
            return Response({"result_search": validated_recipes})
        else: return Response({"result_search": None})

# посмотреть как правильно реализовывать такие системы и что делать с username



# сделать самую простую систему поиска и в дальнейшем добавить туда влияние рейтинга.
# от рейтинга будет зависеть на каком месте будет расположен рецепт