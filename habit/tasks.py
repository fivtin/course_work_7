from celery import shared_task

from habit.services import send_tgm_message


@shared_task
def telegram_auto_sending():
    if False:
        send_tgm_message(None, None)

    # users = User.objects.filter(is_active=True, last_login__lte=datetime.now() - timedelta(days=30))
    # for user in users:
    #     user.is_active = False
    #     user.save()
