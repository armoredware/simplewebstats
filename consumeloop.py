#!/usr/bin/python

import datetime
import time
import os
import sqlite3
from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess

#def to_matrix(l, n):
    #return [l[i:i+n] for i in range(0, len(l), n)]


def consume_stats():
    print("Ready...")
    subprocess.call("consumerawstats.py", shell=True)
    '''fo = open("//web121/g$/web_stats.txt", "r+", errors='ignore')
    strstats = fo.read();
    filedate = str(time.time())
    newfile = "//web121/g$/webstats" + filedate + ".txt"
    
    try:
        os.rename( "//web121/g$/web_stats.txt", newfile)
        print("web stats archived")
    except:
        os.remove("//web121/g$/web_stats.txt")
        print('failed, deleting stats file to avoid duplicates')
    

    stat_arry = strstats.split(',')
    stat_arry.pop()
    stats = to_matrix(stat_arry, 3)
    conn = sqlite3.connect('webstats.db')
    print ("Opened database successfully")

    x = 0
    for stat in stats:
        print (stat[0],stat[1],stat[2])
    try:
        conn.execute("INSERT INTO RAWSTATS (PAGEURL,CLIENTIP,DATE) \
            VALUES (?,?,?)",(stat[0], stat[1], stat[2]))
    except Exception as e:
        print ("most records inserted", e)

    conn.commit()
    print ("Records created successfully")
    conn.close()'''


scheduler = BlockingScheduler()
scheduler.add_job(consume_stats, 'interval', hours=.2)
scheduler.start()