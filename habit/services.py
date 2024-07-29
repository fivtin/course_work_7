import requests

from config.settings import TELEGRAM_URL, TELEGRAM_BOT_TOKEN


def send_tgm_message(chat_id, text):
    params = {
        'text': text,
        'chat_id': chat_id
    }
    requests.get(f'{TELEGRAM_URL}{TELEGRAM_BOT_TOKEN}/sendMessage', params)
