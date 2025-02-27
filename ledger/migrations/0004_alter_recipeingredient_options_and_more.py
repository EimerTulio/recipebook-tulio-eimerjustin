# Generated by Django 5.1.6 on 2025-02-27 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0003_alter_ingredient_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipeingredient',
            options={'verbose_name': 'recipe_ingredient', 'verbose_name_plural': 'recipe_ingredients'},
        ),
        migrations.AlterUniqueTogether(
            name='recipeingredient',
            unique_together={('recipe', 'ingredient', 'quantity')},
        ),
    ]
