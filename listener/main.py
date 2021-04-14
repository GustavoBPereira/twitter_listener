import sys

import tweepy

from authentication import twitter_api


class MyStreamListener(tweepy.StreamListener):

    def __init__(self, output_file=sys.stdout):
        super(MyStreamListener, self).__init__()
        self.output_file = output_file

    def on_error(self, status_code):
        print('Error:')
        print(status_code)
        return False

    def on_status(self, status):
        print('>' * 20)
        print(status.text)
        print('>' * 20)

    def on_delete(self, status_id, user_id):
        print('Deleted tweet')
        print(f'status_id: {status_id}')
        print(f'user_id: {user_id}')


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
