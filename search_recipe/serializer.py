from rest_framework import serializers
from create_recipes.models import Recipe


class SearchRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'created_by']