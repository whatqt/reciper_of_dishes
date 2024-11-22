from rest_framework import routers
from django.urls import path, include
from recipes.views import Recipe
from my_recipes.views import MyRecipe, MyRecipes
from update_recipes.views import UpdateMyRecipe
from delete_recipe.views import DeleteRecipe
from all_recipes.views import AllRecipes
from search_recipe.views import SearchRecipeForTitle, ResultSearchRecipeForTitle
from put_stars.views import PutStars



router = routers.DefaultRouter()


urlpatterns = [
    path("recipe/<int:id_recipe>", Recipe.as_view()),
    path("search_recipe/", SearchRecipeForTitle.as_view()),
    path("search_recipe_result/", ResultSearchRecipeForTitle.as_view()),
    path("put_stars/", PutStars.as_view()),
    path("recipes/", AllRecipes.as_view()),
    path("delete_recipe/<title>", DeleteRecipe.as_view()),
    path("update_recipe/<title>", UpdateMyRecipe.as_view()),
    path("my_recipe/<title>", MyRecipe.as_view()),
    path("my_recipes/", MyRecipes.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls))
]

