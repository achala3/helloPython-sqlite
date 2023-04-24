import  sqlite3
conn=sqlite3.connect('C:/mycode/venvWorkSPace/tst.db')

with conn:   #conn.close()를 내포한  with문
    
    cur = conn.cursor()
    sql="select * from score where 이름=? or 성적<=?"
    # precompiled 구문 -> 반복 실행시 속도를 높여준다


    cur.execute(sql,('홍길동',53))
    rows = cur.fetchall()
    
    for row in rows:
        print(row)
