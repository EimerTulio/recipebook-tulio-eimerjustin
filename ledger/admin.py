from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Recipe, RecipeIngredient, Profile

# Register your models here.

class RecipeIngredientInline(admin.TabularInline):
    """Puts recipe ingredients as an inline for admin."""
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    """Lists all recipe names and their contents."""
    model = Recipe
    inlines = [RecipeIngredientInline]

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Recipe, RecipeAdmin)
