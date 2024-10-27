from rest_framework import routers
from django.urls import path, include
from create_recipes.views import CrateRecipe
from my_recipes.views import MyRecipes

router = routers.DefaultRouter()


urlpatterns = [
    path("create_recipe", CrateRecipe.as_view()),
    path("my_recipes/<title>", MyRecipes.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls))
]

