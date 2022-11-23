from django.contrib import admin

from .models import Subscribe, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Регистрация модели User в интерфейсе администратора."""

    list_display = (
        'id',
        'email',
        'username',
        'first_name',
        'last_name',
        'role'
    )
    search_fields = ('username', 'role',)
    list_filter = ('email', 'username',)


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    """Регистрация модели Subscribe в интерфейсе администратора."""

    list_display = ('id', 'user', 'author')
    search_fields = ('user',)
    list_filter = ('user', )
