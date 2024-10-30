from rest_framework import serializers
from create_recipes.models import Recipe
from django.contrib.auth.models import User
from rest_framework import serializers


class MyRecipeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        exclude = ['created_at', 'starts', 'created_by']
    
    # обновление update необходимо, поскольку нам не нужен поле с username создателя. Поэтому обновляем через ORM
    # через базовый update Это не работает
    def update(self, validated_data: dict, title):
        recipe = Recipe.objects.filter(title=title)
        recipe_values = recipe.get(title=title)
        recipe.update(
            title = validated_data.get("title", recipe_values.title),
            ingredients = validated_data.get("ingredients", recipe_values.ingredients),
            instructions = validated_data.get("instructions", recipe_values.instructions),
            categories = validated_data.get("categories", recipe_values.categories),
        )
        return recipe
    
