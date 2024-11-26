from rest_framework import status
from django.shortcuts import redirect
from rest_framework.views import Response
from rest_framework.views import APIView, Request
from .serializer import GetRecipeSerializer
from django.contrib.auth.models import User
from recipes.models import Recipe
from django.core.exceptions import ObjectDoesNotExist
from recipes.service import RightsToDeleteOrPatchOrGet
from .service import GetMyRecipes, IterationRecipes



class MyRecipe(APIView):
    def get(self, request: Request, id_recipe = 0):
        if id_recipe != 0:
            rights_get = RightsToDeleteOrPatchOrGet(
                id_recipe,
                request.user.pk
            )
            if rights_get.chek():
                data_recipe = rights_get.recipe_get()
                serializer = GetRecipeSerializer(
                    data={
                        "title": data_recipe.title,
                        "ingredients": data_recipe.ingredients,
                        "instructions": data_recipe.instructions,
                        "created_at": data_recipe.created_at,
                        "stars": data_recipe.stars,
                        "categories": data_recipe.categories
                    }
                )
                if serializer.is_valid():
                    return Response(
                        {"data_recipe": serializer.data},
                        status.HTTP_302_FOUND 
                    ) 
                return Response(
                    {"Error": "500 Internal Server Error"},
                    status.HTTP_500_INTERNAL_SERVER_ERROR
                )    
            return Response(
                {"data_recipe": rights_get},
                status.HTTP_404_NOT_FOUND
            )

        elif id_recipe == 0: 
            recipes = GetMyRecipes(
                request.user.pk
            )
            recipes = recipes.get_recipes()
            if recipes is None:
                return Response(
                    {"Error": "404 Not Found"},
                    status.HTTP_404_NOT_FOUND
                )
            iteration_recipes = IterationRecipes(
                recipes,
                GetRecipeSerializer
            )
            recipes = iteration_recipes.iteration()
            if recipes:
                return Response(
                    {"recipes": recipes},
                    status.HTTP_302_FOUND
                )
            return Response(
                {"Error": "500 Internal Server Error"},
                status.HTTP_500_INTERNAL_SERVER_ERROR
            )

            
            

       

                    


# сделать еще фильтрацию, а именно поиск по рейтингу, по дате создания, по названию (в афлавитном порядке)