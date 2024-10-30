from rest_framework import routers
from django.urls import path, include
from create_recipes.views import CrateRecipe
from my_recipes.views import MyRecipes
from update_recipes.views import UpdateMyRecipe
from delete_recipe.views import DeleteRecipe
from all_recipes.views import AllRecipes


router = routers.DefaultRouter()


urlpatterns = [
    path("create_recipe", CrateRecipe.as_view()),
    path("recipes", AllRecipes.as_view()),
    path("delete_recipe/<title>", DeleteRecipe.as_view()),
    path("update_recipe/<title>", UpdateMyRecipe.as_view()),
    path("my_recipes/<title>", MyRecipes.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls))
]

