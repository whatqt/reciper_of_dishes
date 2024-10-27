from rest_framework import serializers
from create_recipes.models import Recipe



class GetRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        exclude = ['created_by']
        