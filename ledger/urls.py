from django.urls import path
from .views import recipe_list, recipe

urlpatterns = [
    path('recipes/list', recipe_list, name="recipe-list"),
    path('recipe/<int:recipe_number>', recipe, name="recipe" ),
]

app_name = "ledger"