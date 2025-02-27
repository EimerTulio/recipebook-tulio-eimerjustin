from django.urls import path
from .views import  recipe, RecipeListView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name="recipe-list"),
    path('recipe/<int:pk>', recipe, name="recipe" ),
]
app_name = "ledger"