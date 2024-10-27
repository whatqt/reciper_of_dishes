from rest_framework import status
from django.shortcuts import redirect
from rest_framework.views import Response
from rest_framework.views import APIView, Request
from django.db import connection
from django.http import HttpRequest
from .serializer import CreateRecipeSerializer
from .models import Recipe
from django.contrib.auth.models import User



class CrateRecipe(APIView):
    def post(self, request: Request):
        serializer = CreateRecipeSerializer(data=request.data)
        request.data["created_by"] = request.user.pk
        print(serializer)
        print(request.data)
        if serializer.is_valid():
            serializer.save()  # Передаем объект пользователя
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        