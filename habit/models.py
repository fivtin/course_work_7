from django.db import models

from config import NULLABLE
from users.models import User


# Create your models here.


class Habit(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='пользователь'
    )

    action = models.CharField(
        max_length=255,
        verbose_name='действие'
    )
    when = models.TimeField(
        **NULLABLE,
        verbose_name='время'
    )
    place = models.CharField(
        max_length=255,
        verbose_name='место'
    )

    is_pleasant = models.BooleanField(
        default=False,
        verbose_name='приятная'
    )

    related_to = models.ForeignKey(
        'Habit',
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name='связанная привычка'
    )

    reward = models.CharField(
        max_length=512,
        **NULLABLE,
        verbose_name='вознаграждение'
    )

    period = models.PositiveSmallIntegerField(
        default=1,
        verbose_name='периодичность (дней)'
    )
    duration = models.PositiveSmallIntegerField(
        default=120,
        verbose_name='продолжительность (секунд)'
    )

    is_public = models.BooleanField(
        default=False,
        verbose_name='публичная'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'

    def __str__(self):
        return f'{self.user.email} - {self.action} {self.when} {self.place}'
