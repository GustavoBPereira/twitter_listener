import requests
from decouple import config


def send_message_to_chat(bot_message):
    bot_token = config('TELEGRAM_BOT_TOKEN')

    bot_chatID = config('CHAT_ID')
    send_text = f'https://api.telegram.org/' \
                f'bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={bot_message}'

    response = requests.get(send_text)

    return response.json()


if __name__ == '__main__':
    send_message_to_chat('Testing 123...')
