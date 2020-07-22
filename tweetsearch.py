import json
import os, sys
from datetime import datetime
from time import sleep
import pandas as pd
from requests_oauthlib import OAuth1Session
import psycopg2

from logging import getLogger, StreamHandler, DEBUG

# DBに取得済みのTweetを検索し、なければTwitter APIで検索を実行
# keyword: 必須
def gettweet(keyword):
    # 入力値のcheck
    # keyword: null check
    if not keyword:
        print('検索用keywordが空です')
        # returnでも可(この場合大差ない)
        sys.exit(1)

    # このあたりはenvにまとめてloadenvさせたいところ(オペミス防止)
    CK = '***************'
    CS = '***************'
    AT = '***************'
    ATS = '***************'
    twitter = OAuth1Session(CK, CS, AT, ATS)
    conn = psycopg2.connect("host = localhost port = 5432 dbname = twitter user = postgres password = hoge") 
    cur = conn.cursor()
    cur.execute("select max(tweet_id),min(tweet_id) from tweet_search")
    max_and_since = cur.fetchall()
    
    #max_id
    if max_and_since[0][1] is None:
        max_id = - 1
    else:
        max_id = max_and_since[0][1] - 1
    
    #since_id
    if max_and_since[0][0] is None:
        since_id = None
    else:
        since_id = max_and_since[0][0]

    url = "https://api.twitter.com/1.1/search/tweets.json"
    params = {'q' : keyword, 'count' : 100}

    response = {}
            
    if max_id != -1:
        params['max_id'] = max_id

    if since_id is not None:
        params['since_id'] = since_id
    
    req = twitter.get(url, params = params)

    if req.status_code != 200:
            # 取得失敗時
        print('エラーが出たので15分待ってね！\nstatus code: {}').format(req.status_code)
        sleep(15*60)

    else:
            # status code 200
            # 検索結果のjsonを抽出
        response = json.loads(req.text)
            
            # Pythonのリストは空だとFalse返してくるので、それを利用
        if not response['statuses']:
                # 結果なしパターン
            cur.close()
            conn.close()
            print('キーワードにマッチするツイートがなかったようです。')
            return

            # 1ツイートごとにDBに追加
        for i, tweet in enumerate(response["statuses"]):
            dt = datetime.strptime(tweet["created_at"],"%a %b %d %H:%M:%S %z %Y")
            dt = dt.astimezone()
            dst = datetime.strftime(dt, '%Y-%m-%d %H:%M:%S')
            if not tweet["entities"]["user_mentions"]:
                mention = False
            else:
                mention = True
            cur.execute("insert into tweet_search(tweer_id,\
            name_id, tweet_contents, tweet_profile,\
            follower,tweet_time,quoted,retweet_count,\
                    favorite_count,mention) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",\
                        (tweet["id_str"],tweet["user"]["screen_name"],tweet["text"],tweet["user"]["description"],tweet["user"]["followers_count"],dst,tweet["is_quote_status"],tweet["retweet_count"],mention
                        )
            )
            conn.commit
            
                # ここではconnectionクローズしない
                
            # 追加終了処理
    
    cur.close()
    conn.close() 
            
        
if __name__ == "__main__":
    print("調べたい言葉を入れてね")
    keyword = input()
    gettweet(keyword)

