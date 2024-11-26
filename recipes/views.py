from rest_framework import status
from rest_framework.views import Response
from rest_framework.views import APIView, Request
from .serializer import CreateRecipeSerializer, \
    GetRecipeSerializer, PatchRecipeSerializer
from .models import Recipe
from recipes_of_dishes.decorators import add_created_by_post
from .service import GetRecipe, RightsToDeleteOrPatchOrGet, \
    IterationRecipesAtId



class Recipes(APIView):
    def get_queryset(self):
        recipes = Recipe.objects.all().values()
        return recipes
    
    def get(self, request: Request, id_recipe: int = 0):
        if id_recipe != 0:
            get_recipe = GetRecipe(id_recipe)
            recipe = get_recipe.recipe_filter()
            if recipe:
                recipe = get_recipe.recipe_values()
                created_by = recipe["created_by_id"]
                recipe["created_by"] = created_by
                serializer = GetRecipeSerializer(data=recipe)
                if serializer.is_valid():
                    return Response(
                        serializer.data, 
                        status.HTTP_302_FOUND
                    )
                return Response(
                    serializer.errors,    
                    status.HTTP_400_BAD_REQUEST
                )
            return Response(
                {"Error": "Not Found"},
                status.HTTP_404_NOT_FOUND
            )
        
        elif id_recipe == 0:
            recipes = self.get_queryset()
            iteration_recipes = IterationRecipesAtId(
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

    @add_created_by_post
    def post(self, request: Request):
        serializer = CreateRecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(
                serializer.data, 
                status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, 
            status.HTTP_400_BAD_REQUEST
        )
    
    def delete(self, request: Request, id_recipe: int):
        rights_to_delete = RightsToDeleteOrPatchOrGet(
            id_recipe, 
            request.user.pk
        )
        recipe = rights_to_delete.chek()
        if recipe:
            recipe.delete()
            return Response(
                {recipe.title: "delete"},
                status.HTTP_202_ACCEPTED
            )
        return Response(
            {"Error": "Access denied"}, 
            status.HTTP_403_FORBIDDEN
        )

    def patch(self, request: Request, id_recipe: int):
        rights_to_update = RightsToDeleteOrPatchOrGet(
            id_recipe,
            request.user.pk
        )
        if rights_to_update.chek():
            serializer = PatchRecipeSerializer(
                data=request.data
            )
            if serializer.is_valid():
                serializer.update(
                    serializer.validated_data,
                    request.user.pk,
                    id_recipe
                )
                return Response(
                    {"recipe": "update"}
                )
            return Response(
                serializer.errors
            )
        return Response(
            {"Error": "Not Found"},
            status.HTTP_403_FORBIDDEN
        )



#{"title": "testtttt", "ingredients": "test", "instructions": "test", "categories":["Закуски"]}

#{"title": "test", "ingredients": "test", "instructions": "test", "categories":["Закуски"]}
