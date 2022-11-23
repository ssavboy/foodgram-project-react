from django.core.exceptions import ValidationError


def validate_amount(value):
    if value <= 0:
        raise ValidationError(
            'Количество ингредиентов '
            'не может быть отрицательным или равняться 0.'
        )


def validate_cooking_time(value):
    if value < 1:
        raise ValidationError(
            'Минимальное время приготовления 1 минута.'
        )
