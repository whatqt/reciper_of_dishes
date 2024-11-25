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