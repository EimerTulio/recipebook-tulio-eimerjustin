from django.urls import path
from .views import recipe_list, recipe, RecipeListView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name="recipe-list"),
    path('recipe/<int:recipe_number>', recipe, name="recipe" ),
]

app_name = "ledger"