import sys

import tweepy

from authentication import twitter_api
from telegram_bot.main import send_message_to_chat


class MyStreamListener(tweepy.StreamListener):

    def __init__(self, output_file=sys.stdout):
        super(MyStreamListener, self).__init__()
        self.output_file = output_file

    def on_error(self, status_code):
        print('Error:')
        print(status_code)
        return False

    def on_status(self, status):
        msg = f'{status.user.screen_name}:\n'
        msg += f'{status.text}'
        send_message_to_chat(msg)

    def on_delete(self, status_id, user_id):
        msg = f'Tweet deletado\n'
        msg += f'User id:{user_id}'
        send_message_to_chat(msg)


if __name__ == '__main__':
    listener = MyStreamListener()
    stream = tweepy.Stream(auth=twitter_api.auth, listener=listener)
    try:
        print('starting')
        stream.filter(follow=["841403804109148160"])
    except KeyboardInterrupt:
        print("Stopped.")
    finally:
        print('Done.')
        stream.disconnect()
