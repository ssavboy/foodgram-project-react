from django.http import HttpResponse
from prettytable import PrettyTable


def table_recipes(ingredients):
    table = PrettyTable()
    table.field_names = [
        'Ингридиенты', 'Единицы измерения', 'Количество',
    ]
    for i in ingredients:
        table.add_row([
            i['ingredient__name'],
            i['ingredient__measurement_unit'],
            i['amount'],
        ])
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="ingredients.txt"'
    response.write(table.get_string())
    return response
