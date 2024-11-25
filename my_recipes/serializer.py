from rest_framework import serializers
from recipes.models import Recipe



class GetRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        exclude = ['created_by', 'id']
        

        