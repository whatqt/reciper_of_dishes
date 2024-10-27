from rest_framework import serializers
from .models import Recipe
from django.contrib.auth.models import User
from rest_framework import serializers


class CreateRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        exclude = ['id', 'created_at']
        # fields = ['title', 'ingredients', 'instructions', 'created_by']
        
    # def validate_title(self, value):

    #     if isinstance(value, User) is False:
    #         raise serializers.ValidationError("Test")
    #     return value

    # def create(self, validated_data):
    #     return Recipe.objects.create(**validated_data)