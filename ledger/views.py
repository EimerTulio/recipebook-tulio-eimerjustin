from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('a')

def recipes(request):
    ctx = {
        "recipes:" [
            "list"
            "recipe 1",
            "recipe 2"
        ]
    }
    return render(request, "recipes.html", ctx)