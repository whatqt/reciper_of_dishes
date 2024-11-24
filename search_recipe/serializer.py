from rest_framework import serializers
from recipes.models import Recipe


class SearchRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'created_by']

class ResultSearchRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        exclude = ['id']