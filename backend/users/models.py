from django.contrib.auth.models import AbstractUser
from django.db import models

from .const import (ADMIN, MODERATOR, ROLES, SYMBOLS_150, SYMBOLS_254,
                    SYMBOLS_MESSAGE, USER)
from .mixins import validate_username


class User(AbstractUser):
    """Модель пользователя"""

    email = models.EmailField(
        'Адрес электронной почты',
        max_length=SYMBOLS_254,
        help_text=f'{SYMBOLS_MESSAGE} {SYMBOLS_254}.',
        unique=True
    )
    username = models.CharField(
        'Имя пользователя',
        max_length=SYMBOLS_150,
        help_text=f'{SYMBOLS_MESSAGE} {SYMBOLS_150}.',
        unique=True,
        validators=(
            validate_username,
        )
    )
    password = models.EmailField(
        'Пароль',
        max_length=SYMBOLS_150,
        help_text=f'{SYMBOLS_MESSAGE} {SYMBOLS_150}.'
    )
    first_name = models.CharField(
        'Имя',
        max_length=SYMBOLS_150,
        help_text=f'{SYMBOLS_MESSAGE} {SYMBOLS_150}.'
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=SYMBOLS_150,
        help_text=f'{SYMBOLS_MESSAGE} {SYMBOLS_150}.'
    )
    role = models.CharField(
        'Роль',
        max_length=max([len(value) for key, value in ROLES]),
        choices=ROLES,
        default=USER,
        blank=True
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    @property
    def is_admin(self):
        return self.role == ADMIN or self.is_staff or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == MODERATOR

    def __str__(self):
        return self.username


class Subscribe(models.Model):
    """Модель подписки"""

    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        related_name='follower',
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        related_name='following',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'author',),
                name='unique_subscribe'
            ),
        )
