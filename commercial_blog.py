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

consumer_key = 'consumer key'
consumer_secret = 'consumer secret'
access_token = 'access token'
access_token_secret = 'access token secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit = True)


# -

def main():
    api.update_status("面白そうな事に手を出して、記事にしてるブログ 3PySciを運営中！\n\nPythonやガジェットなどを初心者目線で解説してます。\n\nhttp://3pysci.com\n\nツイッターでは適当に呟きつつ、APIを使って感謝砲を毎日（テスト）発動中です。")


if __name__ == '__main__':
    main()
