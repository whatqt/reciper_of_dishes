from rest_framework import serializers
from recipes.models import Recipe
from .logic_stars import RecipeStars


class PutStarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['title', 'stars', 'created_by']

    def update(self, recipe, data_recipe, validated_data):
        current_rating = int(data_recipe.stars)
        print(data_recipe.stars)
        if current_rating == 0.0:
            current_rating = []
        rating_update = RecipeStars([current_rating])
        print(validated_data["stars"])
        print(type(validated_data["stars"]))
        rating_update.add_stars(float(validated_data["stars"]))
        change_stars = rating_update.calculate_average_stars()
        recipe.update(stars=change_stars)
        return recipe