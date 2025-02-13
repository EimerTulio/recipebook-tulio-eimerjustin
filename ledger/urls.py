from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('recipes', recipes, name="recipe-list"),
]

app_name = "ledger"