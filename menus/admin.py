from django.contrib import admin
from .models import Menu, Recipe, Ingredient, RecipeIngredient

# Register your models here.
admin.site.register(Menu)
admin.site.register(Recipe)
admin.site.register(Ingredient)