from rest_framework import serializers
from .models import Recipe
from django.contrib.auth.models import User
from rest_framework import serializers
from .service import ValidateType



class CreateRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        exclude = ['created_at', 'id']
        
    def validate_categories(self, value):
        categories = ValidateType().get_validate_categories()
        len_value = len(value)
        if len_value == 0:
            raise serializers.ValidationError("no categories selected")
        for number_recipe in range(len_value):
            if value[number_recipe].lower() not in categories:
                raise serializers.ValidationError(f"The {value[number_recipe]} category does not exist")
        return value

class GetRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'
        
class PatchRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        exclude = ['created_at', 'stars', 'created_by', 'id']

    def update(self, validated_data: dict, user, id_recipe):
        recipe = Recipe.objects.filter(created_by=user, id=id_recipe)
        recipe.update(
            title = validated_data.get("title", validated_data["title"]),
            ingredients = validated_data.get("ingredients", validated_data["ingredients"]),
            instructions = validated_data.get("instructions", validated_data["instructions"]),
            categories = validated_data.get("categories", validated_data["categories"]),
        )
        return recipe






# {"title": "test", "ingredients": "test", "instructions": "test", "categories": ["Закуски"], "created_by": "admin"}