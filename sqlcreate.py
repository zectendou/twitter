import psycopg2
import os

def intodatabase(ID, tweets, dates):
    conn = psycopg2.connect("host = localhost port = 5432 dbname = twitter user = postgres password = hogehoge") 
    cur = conn.cursor()
    cur.execute("INSERT INTO hoge (ID, tweets, dates) VALUES (%s, %s, %s)",(tweet_id,dst,tweet_contents))
    cur.close()
    conn.close() 
    return

