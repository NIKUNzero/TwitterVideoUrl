# -*- coding: utf-8 -*-

import random
import time
import tweepy
import config

CK = config.CK
CS = config.CS
AT = config.AT
ATS = config.ATS

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, ATS)

api = tweepy.API(auth)

PlusWords = ['すごい！', 'この動画凄い！', 'これはすごい！', 'これはやべぇ！', 'あわわわわわわ', 'ﾃﾞｭﾌﾌｗｗｗｗｗ', 'かわいい！', '♡', '😘😘', 'やば！！！', 'こｗれｗはｗ', 'すごいｗｗｗｗｗ', '＾３＾']
VideoAccounts = ['planetpng', 'petloveri', 'kyounoiyashi', 'dobutsu_iyashi','mohu_Movie', 'iyashichannel_', 'Kawaiipettv', 'After100days', 'mofnekoclub']
sleepsecond = [86400, 87400, 129600, 110600, 93428, 92381, 125312]
sleeptime = int(random.choice(sleepsecond))

while True:
    for status in api.user_timeline(random.choice(VideoAccounts), count=1, include_rts=False):
        if hasattr(status, 'extended_entities'):
            for media in status.extended_entities.get('media', [{}]):
                if media.get('type', None) == 'video':
                    media_url = media['url']
                    api.update_status(random.choice(PlusWords) + str(media_url))
                    print(random.choice(PlusWords) + str(media_url))
                    time.sleep(sleeptime)