from .models import Recipe
from django.core.exceptions import ObjectDoesNotExist
from my_recipes.service import IterationRecipes


class ValidateType:
    def get_validate_categories(self):
        categories = [
            "закуски",
            "первые блюда",
            "вторые блюда",
            "салаты",
            "десерты",
            "напитки"
        ]
        return categories
    
class GetRecipe:
    def __init__(self, id_recipe):
        self.id_recipe = id_recipe

    # найти как решить дилему:
    # какое лучше дать название или сделать два метода:
    # один метод возращает сам объект, а второй возращает объекты/dict
    def recipe_get(self):
        try:
            recipe = Recipe.objects.filter(
                id=self.id_recipe
            )
            return recipe
        except ObjectDoesNotExist: 
            return None

class RightsToDeleteOrPatchOrGet:
    def __init__(self, id_recipe, id_user):
        self.id_recipe = id_recipe
        self.id_user = id_user

    def chek(self):
        try:
            chek_rights = Recipe.objects.filter(
                created_by_id=self.id_user,
                id=self.id_recipe
            ).get()
            return chek_rights
        except ObjectDoesNotExist:
            return None

class IterationRecipesAtId(IterationRecipes):
    def iteration(self):
        super().iteration()
        validate_recipes = []
        for recipe in self.recipes:
            created_by = recipe["created_by_id"] 
            del recipe["created_by_id"] 
            recipe["created_by"] = created_by
            serializer = self.class_serializer(
                data=recipe
            )
            if serializer.is_valid() is False:
                return False
            else: validate_recipes.append(recipe)

        return validate_recipes
