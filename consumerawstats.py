#!/usr/bin/python

import datetime
import time
import os
import sqlite3

def to_matrix(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]





# Open raw stats file
#fo = open("//web121/g$/webstats1465309325.5318573.txt", "r+", errors='ignore')
#fo = open("//web121/g$/web_stats.txt", "r+", errors='ignore')
fo = open("web_stats.txt", "r+", errors='ignore')
#fo = open("//web121/g$/web_stats.txt", "r+")

strstats = fo.read();
#print ("Read String is : ", str)
# Close opened file
fo.close()

# Rename webstats
filedate = str(time.time())
#newfile = "//web121/g$/webstats" + filedate + ".txt"
#print(newfile)
'''try:
    os.rename( "web_stats.txt", newfile)
    print("web stats archived")
except:
    os.remove("//web121/g$/web_stats.txt")
    print('failed, deleting stats file to avoid duplicates')
'''    

stat_arry = strstats.split(',')
#last entry removal because its blank
stat_arry.pop()
#turn into an array
stats = to_matrix(stat_arry, 3)
#print(stats[0])
#print(stats[0][0])



conn = sqlite3.connect('webstats.db')
print ("Opened database successfully")

x = 0
for stat in stats:
    #print(stat)
    #surl = x + 0
    #sip = x + 1
    #sdate = x + 2
    print (stat[0],stat[1],stat[2])
    try:
        conn.execute("INSERT INTO RAWSTATS (PAGEURL,CLIENTIP,DATE) \
            VALUES (?,?,?)",(stat[0], stat[1], stat[2]))
    except Exception as e:
        print ("most records inserted", e)

conn.commit()
print ("Records created successfully")
conn.close()


#tranform datetime
#input data into table
#output stats to html format

