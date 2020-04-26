import json
import os
from datetime import datetime
from time import sleep
import pandas as pd



def gettweet(keyword, max_id, since_id)
CK = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
CS = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
AT = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ATS = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
twitter = OAuth1Session(CK, CS, AT, ATS)
max_id = -1
url = "https://api.twitter.com/1.1/search/tweets.json"
params = {'q' : keyword, 'count' : 100, 'max_id': max_id}



while(True):
    if max_id != -1:
        params['max_id'] = max_id
        req = twitter.get(url, params = params)
    

        if req.status_code ==200:
            tweets = json.loads(req.text)
        
            if tweets['statuses'] ==[]:
                break
                



            for tweet in tweets["statuses"]:
                tweet_id = int(tweet["id_str"])
                name_id = tweet["screenname"]
                twitter_name = tweet["name"]
                tweet_contents  = tweet["full_text"]
                tweet_profile = tweet["description"]
                follower = tweet[""]
                tweettime = datetime.strptime(tweet["created_at"], '%a %b %d %H:%M:%S %z %Y')
                tweet_datetime = tweettime.datetime('%Y, %m, %d, %H,%M,%S')))
                if tweets.get("extended_entities"]:
                    media_list = tweet['extended_entities']["media"]
                    for media in media_list:
                        media_type = media_list["type"]
                        media_url = media_type["expanded_url"]
                if tweets.get["extended_entities"]:
                    url_list = tweet["extended_entities"]
                    for  url in url_list:
                        link = url_list["url"]
                favorite_count = tweet["favoriet_count"]
                quoted = tweet["is_quate_status"]
                retweet = tweet["retweet_count"]
                mention = tweet[]"usermention"]


            max_id = tweets['statuses'][-1]['id']
        
        else:
            print('15分待ってね！')
            sleep(15*60)



    
    
