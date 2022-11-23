from django.contrib.auth import get_user_model
from django.db import models

from .mixins import validate_amount, validate_cooking_time

User = get_user_model()


class Tag(models.Model):
    """Модель тега"""

    name = models.CharField(
        'Название',
        max_length=255,
        unique=True
    )
    color = models.CharField(
        'Цвет',
        max_length=7,
        unique=True
    )
    slug = models.SlugField(
        'Эндпоинт',
        max_length=255,
        unique=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Модель ингредиента"""

    name = models.CharField(
        'Название',
        max_length=200
    )
    measurement_unit = models.CharField(
        'Единицы измерения',
        max_length=200,
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Модель рецепта"""

    ingredients = models.ManyToManyField(
        Ingredient,
        verbose_name='Ингредиенты',
        related_name='recipe'
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Теги'
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        related_name='recipes',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        'Название',
        max_length=255
    )
    image = models.ImageField(
        'Картинка',
        upload_to='recipes/images/'
    )
    text = models.TextField(
        'Текстовое описание'
    )
    cooking_time = models.DateTimeField(
        'Время приготовления в минутах',
        validators=(
            validate_cooking_time,
        )
    )

    class Meta:
        ordering = ('-cooking_time',)
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class IngredientRecipe(models.Model):
    """Промежуточная модель связи Ingredient и Recipe"""

    recipe = models.ForeignKey(
        Recipe,
        verbose_name='Рецепт',
        on_delete=models.CASCADE,
        related_name='ingredient_recipe'
    )
    ingredient = models.ForeignKey(
        Ingredient,
        verbose_name='Ингредиент',
        on_delete=models.CASCADE,
        related_name='ingredient_recipe'
    )
    amount = models.IntegerField(
        'Количество',
        validators=(
            validate_amount,
        )
    )

    class Meta:
        verbose_name = 'Количество ингредиента'
        verbose_name_plural = 'Количество ингредиентов'

    def __str__(self):
        return (f'{self.ingredient.name} - {self.amount}'
                f'{self.ingredient.measurement_unit}')


class Favorite(models.Model):
    """Модель списка избранного"""

    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='favorite_recipe'
    )
    recipe = models.ForeignKey(
        Recipe,
        verbose_name='Рецепт',
        on_delete=models.CASCADE,
        related_name='favorite_recipe'
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'


class ShoppingCart(models.Model):
    """Модель списка покупок"""

    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='shopping_cart',
    )
    recipe = models.ForeignKey(
        Recipe,
        verbose_name='Рецепт',
        on_delete=models.CASCADE,
        related_name='shopping_cart',
    )

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'
