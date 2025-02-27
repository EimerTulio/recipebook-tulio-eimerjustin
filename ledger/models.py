from django.db import models
from django.urls import reverse

# Create your models here.
class Ingredient(models.Model):
    """Model representing an ingredient"""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'ingredient'
        verbose_name_plural = 'ingredients'

class Recipe(models.Model):
    """Model representing a recipe"""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe', args=[self.pk])
    
    class Meta:
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'

class RecipeIngredient(models.Model):
    """Model representing an ingredient of a recipe"""
    ingredient = models.ForeignKey(Ingredient, 
                                   on_delete=models.CASCADE, 
                                   related_name="recipe")   

    quantity = models.CharField(max_length=50) 

    recipe = models.ForeignKey(Recipe, 
                               on_delete=models.CASCADE, 
                               related_name="ingredients")
    
    def __str__(self):
        return self.recipe.name + " " + self.ingredient.name + " " + self.quantity

    class Meta:
        unique_together = ["recipe", "ingredient", "quantity"]
        verbose_name = 'recipe_ingredient'
        verbose_name_plural = 'recipe_ingredients'

