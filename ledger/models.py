from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

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
    author = models.ForeignKey(Profile,
                               on_delete=models.SET_NULL,
                               null=True,
                               related_name='recipe')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

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
        return self.recipe.name + "-" + self.quantity + " " + self.ingredient.name

    class Meta:
        unique_together = ["recipe", "ingredient", "quantity"]
        verbose_name = 'recipe ingredient'
        verbose_name_plural = 'recipe ingredients'
