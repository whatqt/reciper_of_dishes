from recipes.models import Recipe
from django.core.exceptions import ObjectDoesNotExist


class GetMyRecipes:
    def __init__(self, created_by_id):
        self.created_by_id = created_by_id

    def get_recipes(self):
        try:
            recipes = Recipe.objects.filter(
                created_by_id=self.created_by_id
            ).values()
            return recipes
        except ObjectDoesNotExist:
            return None
        
class IterationRecipes:
    def __init__(
            self, recipes, 
            class_serializer
    ):
        self.recipes = recipes
        self.class_serializer = class_serializer
    
    def iteration(self):
        validate_recipes = []
        for recipe in self.recipes:
            serializer = self.class_serializer(
                data=recipe
            )
            if serializer.is_valid() is False:
                return False
            else: validate_recipes.append(recipe)

        return validate_recipes
        
