from rest_framework import status
from django.shortcuts import redirect
from rest_framework.views import Response
from rest_framework.views import APIView, Request
from .serializer import PutStarsSerializer
from django.contrib.auth.models import User
from create_recipes.models import Recipe
from django.core.exceptions import ObjectDoesNotExist



# тут же в будущем можно сделать и добавление коментариев
class PutStars(APIView):
    def get_quaryset(self, title, created_by_id):
        try:
            recipe = Recipe.objects.filter(title=title, created_by_id=created_by_id)
            return recipe
        except ObjectDoesNotExist:
            return {"Recipe": None}
        
    def patch(self, request: Request):
        print(request.data)
        serializer = PutStarsSerializer(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            recipe = self.get_quaryset(
                serializer.validated_data["title"], 
                serializer.validated_data["created_by"]
            )
            print(recipe)
            if recipe:
                data_recipe = recipe.get()
                print(serializer.data)
                serializer.update(recipe, data_recipe, serializer.validated_data) 
                return Response({"Recipe": "The rating has been updated"})
            else: return Response(recipe)
        else: return Response(serializer.errors)


# дальше по планам смотреть код и добавить возможность комментрирования и добавление фоток
{"title": "test", "stars": 5.0, "created_by": 2}