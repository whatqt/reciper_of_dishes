from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class TestRecipe(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    created_by = models.CharField(max_length=128, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)


# подтягивать базу данных и ORM в Django
# сделать адекватное добавление данных и всё через ORM