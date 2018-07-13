import sqlite3


conn = sqlite3.connect('webstats.db')
print ("Opened database successfully")
conn.execute("DELETE from RAWSTATS where id=3003;")
conn.commit
print ("Total number of rows deleted :", conn.total_changes)

conn.close()