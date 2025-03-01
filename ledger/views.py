from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.list import ListView

from .models import Recipe

# Create your views here.

class RecipeListView(ListView):
    "A view that shows list of all recipes."
    model = Recipe
    template_name = 'ledger/recipe_list.html'

def recipe(request, pk):
    "A view that shows the contents of one recipe."
    rcp = Recipe.objects.get(pk=pk)
    ctx = {'ingredients': rcp.ingredients.all()}
    return render(request, "ledger/recipe.html", ctx)
