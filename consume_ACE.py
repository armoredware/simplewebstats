#!/usr/bin/python

import datetime
import time
import os
import sqlite3

def to_matrix(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]





# Open raw stats file
#fo = open("//web121/g$/ace1465309325.5318573.txt", "r+", errors='ignore')
fo = open("//web121/g$/ace.txt", "r+", errors='ignore')
#fo = open("//web121/g$/ace.txt", "r+")

str_ace = fo.read();
#print ("Read String is : ", str)
# Close opened file
fo.close()

# Rename webstats
filedate = str(time.time())
newfile = "//web121/g$/ace" + filedate + ".txt"
#print(newfile)
try:
    os.rename( "//web121/g$/ace.txt", newfile)
    print("web stats archived")
except:
    os.remove("//web121/g$/ace.txt")
    print('failed, deleting stats file to avoid duplicates')
    

qa_arry = str_ace.split('~')
#last entry removal because its blank
qa_arry.pop()
#turn into an array
question = to_matrix(qa_arry, 17)
conn = sqlite3.connect('ace.db')
print ("Opened database successfully")

for field in question:
    print (field[0],field[1],field[2],
    field[3],field[4],field[5],
    field[6],field[7],field[8],
    field[9],field[10],field[11],
    field[12],field[13],field[14],
    field[15],field[16])
    try:
        conn.execute("INSERT INTO ACE (SUBJECT, CATEGORY, LEVEL, QUESTION, MC1, MC2, MC3, MC4, MC5, MC6, ANS1, ANS2, ANS3, ANS4, ANS5, ANS6, EXPLANATION ) \
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(field[0], field[1], field[2],field[3], field[4], field[5],field[6], field[7], field[8],field[9], field[10], field[11],field[12], field[13], field[14],field[15], field[16]))
    except Exception as e:
        print ("most records inserted", e)

conn.commit()
print ("Records created successfully")
conn.close()


#tranform datetime
#input data into table
#output stats to html format

