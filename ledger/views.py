from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Recipe

# Create your views here.

class RecipeListView(ListView):
    """A view that shows list of all recipes."""
    model = Recipe
    context_object_name = 'recipe_list'
    template_name = 'ledger/recipe_list.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    """A view that shows the contents of one recipe."""
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'ledger/recipe.html'
    redirect_field_name = 'ledger:recipe-list'
    
