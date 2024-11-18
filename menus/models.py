from django.db import models

# Create your models here.
class Menu(models.Model):
    category = models.CharField(max_length = 255)
    item_name = models.CharField(max_length = 255)
    price = models.FloatField()
    staff = models.ForeignKey('staff.Staff', on_delete = models.SET_NULL, null=True)

class Recipe(models.Model):
    chef_name = models.CharField(max_length = 255)
    preparation_instrution = models.TextField()


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length = 255)
    quality =models.CharField(max_length = 255)

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete = models.CASCADE)
  