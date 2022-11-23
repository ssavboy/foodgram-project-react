from django.contrib import admin

from .models import Favorite, Ingredient, Recipe, ShoppingCart, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Регистрация модели Tag в интерфейсе администратора."""

    list_display = ('id', 'name', 'color', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """Регистрация модели Ingredient в интерфейсе администратора."""

    list_display = ('id', 'name', 'measurement_unit')
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Регистрация модели Recipe в интерфейсе администратора."""

    list_display = ('id', 'name', 'author')
    search_fields = ('author', 'name', 'tags')


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    """Регистрация модели Favorite в интерфейсе администратора."""
    list_display = ('id', 'user', 'recipe')
    search_fields = ('user',)
    list_filter = ('user',)


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    """Регистрация модели ShoppingCart в интерфейсе администратора."""
    list_display = ('id', 'user', 'recipe')
    search_fields = ('user',)
    list_filter = ('user',)
