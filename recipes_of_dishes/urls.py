from rest_framework import routers
from django.urls import path, include
from recipes.views import Recipes
from my_recipes.views import MyRecipe
from search_recipe.views import SearchRecipeForTitle, ResultSearchRecipeForTitle
from put_stars.views import PutStars



router = routers.DefaultRouter()


urlpatterns = [
    path("recipe/", Recipes.as_view()),
    path("recipe/<int:id_recipe>", Recipes.as_view()),
    path("search_recipe/", SearchRecipeForTitle.as_view()),
    path("search_recipe_result/", ResultSearchRecipeForTitle.as_view()),
    path("put_stars/", PutStars.as_view()),
    path("my_recipe/", MyRecipe.as_view()),
    path("my_recipe/<int:id_recipe>", MyRecipe.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls))
]

