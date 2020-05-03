#備忘録
from datetime import datetime

tweets = {'created_at':'Mon Feb 15 11:31:17 +0000 2020'}

for tweet in tweets

    dt = datetime.strptime(
        tweets['created_at'],'%a %b %d %H:%M:%S %z %Y'
    )

    dt = dt.astimezone()


    dst = datetime.strftime(
        dt, '%Y-%m-%d %H:%M:%S'
    )

