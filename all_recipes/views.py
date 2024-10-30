from rest_framework import status
from django.shortcuts import redirect
from rest_framework.views import Response
from rest_framework.views import APIView, Request
from .serializer import  AllViewRecipeSerializer
from django.contrib.auth.models import User
from create_recipes.models import Recipe
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers