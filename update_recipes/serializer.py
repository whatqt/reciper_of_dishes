from rest_framework import serializers
from create_recipes.models import Recipe
from django.contrib.auth.models import User
from rest_framework import serializers


class MyRecipeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        exclude = ['created_at', 'starts', 'created_by', 'id']
    
    # обновление update необходимо, поскольку нам не нужен поле с username создателя. Поэтому обновляем через ORM
    # через базовый update Это не работает
    def update(self, validated_data: dict, title, user):
        recipe = Recipe.objects.filter(created_by=user)
        recipe_values = recipe.get(title=title)
        recipe.update(
            title = validated_data.get("title", recipe_values.title),
            ingredients = validated_data.get("ingredients", recipe_values.ingredients),
            instructions = validated_data.get("instructions", recipe_values.instructions),
            categories = validated_data.get("categories", recipe_values.categories),
        )
        return recipe
    
    # def validate_categories(self, value):
    #     categories = [
    #         "закуски",
    #         "первые блюда",
    #         "вторые блюда",
    #         "салаты",
    #         "десерты",
    #         "напитки"
    #     ]
        
    #     print(value)
    #     len_value = len(value)
    #     if len_value != 0:
    #         for number_recipe in range(len(value)):
    #             print(value[number_recipe])
    #             if value[number_recipe].lower() not in categories:
    #                 raise serializers.ValidationError(f"The {value[number_recipe]} category does not exist")
    #             else: return value
    #     else: raise serializers.ValidationError("no categories selected")
