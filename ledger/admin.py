from django.contrib import admin

from .models import Recipe, RecipeIngredient

# Register your models here.

class RecipeIngredientInline(admin.TabularInline):
    """Puts recipe ingredients as an inline for admin."""
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    """Lists all recipe names and their contents."""
    model = Recipe
    inlines = [RecipeIngredientInline]

admin.site.register(Recipe, RecipeAdmin)
