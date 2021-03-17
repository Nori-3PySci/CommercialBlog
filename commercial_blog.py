# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.10.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
import tweepy

consumer_key = ' consumer key '
consumer_secret = ' consumer secret '
access_token = ' access token '
access_token_secret = ' access token secret '

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit = True)


# -

def main():
    api.update_status(
"Pythonを中心に色んなことに手を出しているブログ「3PySci」を運営中！\n\n\
プログラミング頑張っている人、一緒に頑張っていきましょう！\n\n\
よろしくお願いします！\n\n\
#Python\n\
#Python初心者\n\
#プログラミング初心者\n\
#ガジェット好き\n\
#Apple好き\n\
http://3pysci.com")

if __name__ == '__main__':
    main()


