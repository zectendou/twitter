#備忘録
from datetime import datetime

tweet = {'created_at':'Mon Feb 15 11:31:17 +0000 2020'}


dt = datetime.strptime(
    tweet['created_at'],'%a %b %d %H:%M:%S %z %Y'
)

dt = dt.astimezone()


dst = datetime.strftime(
    dt, '%Y-%m-%d %H:%M:%S'
)

