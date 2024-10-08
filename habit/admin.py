from django.contrib import admin

from habit.models import Habit


# Register your models here.

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'place', 'when', 'action',
                    'is_pleasant', 'related_to', 'reward',
                    'period', 'duration', 'is_public', )
    list_filter = ('user', 'is_pleasant', 'is_public', )
