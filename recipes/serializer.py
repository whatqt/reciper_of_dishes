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

# {"title": "test", "ingredients": "test", "instructions": "test", "categories": ["Закуски"], "created_by": "admin"}