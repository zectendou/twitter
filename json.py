import json
import os
from datetime import datetime
from time import sleep
import pandas as pd
from requests_oauthlib import OAuth1Session


def gettweet(keyword)
CK = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
CS = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
AT = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ATS = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
twitter = OAuth1Session(CK, CS, AT, ATS)
max_id = -1
url = "https://api.twitter.com/1.1/search/tweets.json"
params = {'q' : keyword, 'count' : 100, 'max_id': max_id, 'since_id': since_id}

#入れ物作り
tweets =  {}
tweet_id = []
name_id = []
twitter_name = []
twitter_name = []
tweet_contents  = []
tweet_profile = []
follower = []
date = []
favorite_count =[]
quoted = []
retweet = []
mention = []




for i, tweet in enumerate(tweets):
    if i >= max_id:
        break

    if max_id != -1:
        params['max_id'] = max_id
        req = twitter.get(url, params = params)
    

        if req.status_code ==200:
            tweets = json.loads(req.text)
        
            if tweets['statuses'] ==[]:
                break

            for tweet in tweets["statuses"]:
                tweet_id.append(int(tweet["id_str"]))
                name_id.append(tweet["screenname"])
                twitter_name.append(tweet["name"])
                tweet_contents.append(tweet["text"])
                tweet_profile.append(tweet["description"])
                follower.append(tweet["follower"])
                dt = datetime.strptime(tweet["created_at"],"%a %b %d %H:%M:%S %z %Y")
                dt = dt.astimezone()
                dst = datetime.strftime(dt, '%Y-%m-%d %H:%M:%S')
                date.append(dst)
                favorite_count.append(tweet["favoriet_count"])
                quoted.append(tweet["is_quate_status"])
                retweet.append(tweet["retweet_count"])
                mention.appendtweet["usermention"])


            max_id = tweet_id - 1 
        
        else:
            print('15分待ってね！')
            sleep(15*60)



    
    
