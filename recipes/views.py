from rest_framework import status
from rest_framework.views import Response
from rest_framework.views import APIView, Request
from .serializer import CreateRecipeSerializer, \
    GetRecipeSerializer, PatchRecipeSerializer
from recipes_of_dishes.decorators import add_created_by_post, add_created_by_get
from .service import GetRecipe, RightsToDeleteOrPatch
import json


class Recipe(APIView):
    @add_created_by_get
    def get(self, request: Request, id_recipe: int):
        get_recipe = GetRecipe(id_recipe)
        recipe = get_recipe.get()
        if recipe:
            recipe.update(request.data)
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
        rights_to_delete = RightsToDeleteOrPatch(
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
        rights_to_update = RightsToDeleteOrPatch(
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
                return Response({"recipe": "update"})
            return Response(serializer.errors)
        return Response(
            {"Error": "Not Found"},
            status.HTTP_403_FORBIDDEN
        )



#{"title": "testtttt", "ingredients": "test", "instructions": "test", "categories":["Закуски"]}

#{"title": "test", "ingredients": "test", "instructions": "test", "categories":["Закуски"]}
