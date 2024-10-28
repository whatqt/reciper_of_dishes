from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField




class Recipe(models.Model):
    title = models.CharField(primary_key=True, max_length=200, db_index=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    starts = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    categories = ArrayField(models.CharField(max_length=61), size=6)
    # добавить судуа поле, где будет показан общий рейтинг, который будет вычитываться по формуле

# добавить суда модель где будут храниться коментарии и оценки, и просмотры(так же через ForeignKey) 
# саму функцию добавление оценки сделать в webapp view_recipes 
# и в ленте рецептов сделать систему, которая будет отслеживать, что лайкнул пользователь. 
# Так же надо будет добавить категории