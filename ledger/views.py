from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.list import ListView

from .models import Recipe, RecipeIngredient

# Create your views here.


class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipe_list.html'

def recipe(request, pk):
    rcp = Recipe.objects.get(pk=pk)
    ctx = {'ingredients': rcp.ingredients.all()}
    return render(request, "ledger/recipe.html", ctx)