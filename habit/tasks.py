from datetime import datetime

from celery import shared_task

from habit.models import Habit
from habit.services import send_tgm_message


@shared_task
def telegram_auto_sending():

    habits = Habit.objects.filter(user__tgm_id__isnull=False)
    for habit in habits:
        if habit.when:
            habit_when = habit.when.strftime("%H:%M")
            now = datetime.now().strftime('%H:%M')
            if habit_when == now:
                text = f"""{habit.when.strftime("%H:%M")} - CЕРВИС ПРИВЫЧЕК:
Время выполнить '{habit.action}' в {habit.place}."""

                if habit.reward:
                    text = f'{text}\nЗа это можно {habit.reward}.'
                elif habit.related_to:
                    text = f'{text}\nЗа это можно {habit.related_to.action}.'

                send_tgm_message(habit.user.tgm_id, text)
