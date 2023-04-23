import  sqlite3
conn=sqlite3.connect('C:/mycode/venvWorkSPace/tst.db')
# conn=sqlite3.connect('tst.db')
cur=conn.cursor()
cur.execute("select * from students")
# cur.execute(".tables")
rows=cur.fetchall()
for row in rows:
    print(row)
conn.close()