import json
import os
from datetime import datetime
from time import sleep
import pandas as pd
from requests_oauthlib import OAuth1Session
import psycopg2


def gettweet(keyword):
    CK = '***************'
    CS = '***************'
    AT = '***************'
    ATS = '***************'
    twitter = OAuth1Session(CK, CS, AT, ATS)
    conn = psycopg2.connect("host = localhost port = 5432 dbname = twitter user = postgres password = hoge") 
    cur = conn.cursor()
    cur.execute("select max(tweet_id) from tweet_search")
    last_tweet = cur.fetchone()
    max_id = -1
    since_id = None if last_tweet is None else last_tweet[0]
    url = "https://api.twitter.com/1.1/search/tweets.json"
    params = {'q' : keyword, 'count' : 100}

    tweets = {}
            

    if max_id != -1:
        params['max_id'] = max_id

    if since_id is not None:
        params['since_id'] = since_id
        req = twitter.get(url, params = params)
        
        if req.status_code == 403:
            cur.close()
            conn.close()
            break


        if req.status_code == 503:
            cur.close()
            conn.close()
            break
        
        if req.status_code == 404:
            cur.close()
            conn.close()
            break


        if req.status_code ==200:
            tweets = json.loads(req.text)
            
            if tweets['statuses'] ==[]:
                cur.close()
                conn.close()
                break

            for tweet in tweets["statuses"]:
                if i >= max_id:
                    cur.close()
                    conn.close()
                   　break

                else dt = datetime.strptime(tweet["created_at"],"%a %b %d %H:%M:%S %z %Y")
                    dt = dt.astimezone()
                    dst = datetime.strftime(dt, '%Y-%m-%d %H:%M:%S')
                    cur.execute("insert into tweet_search(tweer_id,\
                        name_id, tweet_contents, tweet_profile,\
                        follower_count,retweet_count,\
                            quoted,mention,follwer) values",(int(tweet["id_str"]),tweet["screen_name"],tweet["name"],tweet["description"],tweet["favorite_count"],tweet["is_quote_status"],tweet["retweet_count"],tweet["mention"],dst,tweet["text"],tweet['user']['followers_count']
                    ))  
                    conn.commit
                    cur.close()
                    conn.close()         


            max_id = int(tweet["id_str"]) - 1 
            
        else:
            print('15分待ってね！')
            sleep(15*60)
if __name__ == "__main__":
    print("調べたい言葉を入れてね")
    keyword = input()
    gettweet(keyword)

