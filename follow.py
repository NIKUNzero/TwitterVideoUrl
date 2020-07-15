import tweepy
import config
import time

CK = config.CK
CS = config.CS
AT = config.AT
ATS = config.ATS
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print("名前")
        print(status.user.name)
        print("ツイート内容")
        print(status.text)
        try:
            api.create_friendship(user_id)
        except:
            pass
        print("----------------")


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=["#かえでちゃーん"])