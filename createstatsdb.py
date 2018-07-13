#!/usr/bin/python
import sqlite3




conn = sqlite3.connect('webstats.db')
print ("Opened database successfully")

conn.execute("DROP TABLE RAWSTATS;")
print("Table Dropped!")


try:
    conn.execute('''CREATE TABLE RAWSTATS
           (ID INTEGER PRIMARY KEY       AUTOINCREMENT,
           PAGEURL           TEXT    NOT NULL,
           CLIENTIP          TEXT     NOT NULL,
           DATE        TEXT          NOT NULL);''')
           
    print ("Table created successfully")
except:
    print("Table Already Setup")


conn.close()