from rest_framework import status
from rest_framework.views import Response
from rest_framework.views import APIView, Request
from .serializer import CreateRecipeSerializer
from recipes_of_dishes.decorators import add_created_by


class CrateRecipe(APIView):
    @add_created_by
    def post(self, request: Request):
        serializer = CreateRecipeSerializer(data=request.data)
        request.data["created_by"] = request.user.pk
        # serializer.validate_title(request.data["categories"])
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#{"title": "test", "ingredients": "test", "instructions": "test", "categories":["Закуски"]}
