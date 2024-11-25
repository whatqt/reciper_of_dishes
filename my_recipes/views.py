from rest_framework import status
from django.shortcuts import redirect
from rest_framework.views import Response
from rest_framework.views import APIView, Request
from .serializer import GetRecipeSerializer, GetRecipesSerializer
from django.contrib.auth.models import User
from recipes.models import Recipe
from django.core.exceptions import ObjectDoesNotExist
from recipes.service import RightsToDeleteOrPatchOrGet
from .service import GetMyRecipes


class MyRecipe(APIView):
    # def get_queryset(self, title):
    #     try:
    #         return Recipe.objects.filter(created_by=self.request.user).get(title=title)
    #     except ObjectDoesNotExist:
    #         return None

    def get(self, request: Request, id_recipe = 0):
        if id_recipe != 0:
            rights_get = RightsToDeleteOrPatchOrGet(
                id_recipe,
                request.user.pk
            ).chek()
            if rights_get:
                data_recipe = rights_get
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
                print(serializer.is_valid())
                if serializer.is_valid():
                    return Response(
                        {"data_recipe": serializer.data},
                        status.HTTP_302_FOUND 
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
            print(recipes)
            validate_recipes = []
            for recipe in recipes:
                serializer = GetRecipeSerializer(
                    data=recipe
                )
                print(serializer.is_valid())
                if serializer.is_valid() is False:
                    return Response(
                        {"Error": "500 Internal Server Error"},
                        status.HTTP_500_INTERNAL_SERVER_ERROR
                    )
                else: validate_recipes.append(recipe)
            
            return Response({"recipes": validate_recipes})
            

       

                    


# сделать еще фильтрацию, а именно поиск по рейтингу, по дате создания, по названию (в афлавитном порядке)