from rest_framework import serializers
from .models import Recipe
from django.contrib.auth.models import User
from rest_framework import serializers


class CreateRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        exclude = ['created_at']
        
    def validate_categories(self, value):
        categories = [
            "Закуски",
            "Первые блюда",
            "Вторые блюда",
            "Салаты",
            "Десерты",
            "Напитки"
        ]
        
        print(value)
        len_value = len(value)
        if len_value != 0:
            for number_recipe in range(len(value)):
                print(value[number_recipe])
                if value[number_recipe] not in categories:
                    raise serializers.ValidationError(f"The {value[number_recipe]} category does not exist")
                else: return value
        else: raise serializers.ValidationError("no categories selected")

# {"title": "test", "ingredients": "test", "instructions": "test", "categories": ["Закуски"], "created_by": "admin"}