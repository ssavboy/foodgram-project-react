from collections import Counter

from recipes.models import IngredientRecipe
from rest_framework import serializers


def get_shopping_cart(user):
    ingredients = IngredientRecipe.objects.filter(
        recipe__shop_list__user=user.user
    )
    compressed_ingredients = Counter()
    for ing in ingredients:
        compressed_ingredients[
            (ing.ingredient.name, ing.ingredient.measurement_unit)
        ] += ing.amount
    return ([
        f"- {name}: {amount} {measurement_unit}\n"
        for (name, measurement_unit), amount
        in compressed_ingredients.items()
    ])


def validate_tags(tags):
    if not tags:
        raise serializers.ValidationError({
            'tags': 'Тег обязателен для заполнения!'
        })
    tags_set = set()
    for tag in tags:
        if tag in tags_set:
            raise serializers.ValidationError({
                'tags': f'Тег {tag} существует, измените тег!'
            })
        tags_set.add(tag)


def validate_amount(amount):
    if int(amount) < 1:
        raise serializers.ValidationError({
            'amount': 'Количество должно быть больше 0!'
        })


def validate_ingridients(ingredients):
    ingredients_set = set()
    if not ingredients:
        raise serializers.ValidationError({
            'ingredients': 'Ингредиенты обязателены для заполнения!'
        })
    for ingredient in ingredients:
        ingredient_id = ingredient['id']
        if ingredient_id in ingredients_set:
            raise serializers.ValidationError({
                'ingredients': f'Ингредиент {ingredient} существует,'
                ' измените ингредиент!'
            })
        ingredients_set.add(ingredient_id)
        amount = ingredient['amount']
        validate_amount(amount)


def validate_cooking_time(cooking_time):
    if int(cooking_time) < 1:
        raise serializers.ValidationError({
            'cooking_time': 'Время приготовления должно быть больше 0!'
        })
