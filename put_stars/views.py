from rest_framework import status
from django.shortcuts import redirect
from rest_framework.views import Response
from rest_framework.views import APIView, Request
from .serializer import PutStarsSerializer
from django.contrib.auth.models import User
from recipes.models import Recipe
from django.core.exceptions import ObjectDoesNotExist
from recipes.service import GetRecipe



class PutStars(APIView):
    def patch(self, request: Request):
        serializer = PutStarsSerializer(data=request.data)
        if serializer.is_valid():
            recipe = GetRecipe(request.data["id"]).recipe_filter()
            if recipe:
                # recipe = recipe.recipe_filter()
                serializer.update(recipe, serializer.validated_data) 
                return Response(
                    {"Recipe": "The rating has been updated"}, 
                    status.HTTP_202_ACCEPTED
                )
            return Response(
                recipe, 
                status.HTTP_404_NOT_FOUND
            )
        return Response(
            serializer.errors, 
            status.HTTP_400_BAD_REQUEST
        )


#{"id":36, "stars": 5.0}