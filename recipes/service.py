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

    def recipe_filter(self):
        try:
            recipe = Recipe.objects.filter(
                id=self.id_recipe
            )
            return recipe
        except ObjectDoesNotExist: 
            return None
    
    def recipe_values(self):
        recipe = self.recipe_filter()
        if recipe:
            recipe_values = recipe.values()[0]
            return recipe_values
        else: 
            return None


# RightsToDeleteOrPatchOrGet - разделить на 4 класса
class RightsToDeleteOrPatchOrGet:
    def __init__(self, id_recipe, id_user):
        self.id_recipe = id_recipe
        self.id_user = id_user

    def chek(self):
        try:
            chek_rights = Recipe.objects.filter(
                created_by_id=self.id_user,
                id=self.id_recipe
            )
            return chek_rights
        except ObjectDoesNotExist:
            return None
        
    def recipe_get(self):
        check_recipe = self.chek()
        if check_recipe:
            return check_recipe.get()
        else: return None

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
