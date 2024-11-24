from rest_framework import serializers
from recipes.models import Recipe
from .logic_stars import RecipeStars


class PutStarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'stars']

    def update(self, recipe, validated_data):
        recipe_data = recipe.get()
        current_rating = int(recipe_data.stars)
        print(recipe_data.stars)
        if current_rating == 0.0:
            current_rating = float(validated_data["stars"])
        rating_update = RecipeStars([current_rating])
        rating_update.add_stars(float(validated_data["stars"]))
        change_stars = rating_update.calculate_average_stars()
        recipe.update(stars=change_stars)
        return recipe