from rest_framework import serializers
from create_recipes.models import Recipe
from django.contrib.auth.models import User
from rest_framework import serializers


class AllViewRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        exclude = ['id']
        

# {"title": "test", "ingredients": "test", "instructions": "test", "categories": ["Закуски"], "created_by": "admin"}