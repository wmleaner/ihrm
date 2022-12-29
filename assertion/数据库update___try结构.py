import pymysql
conn=None
cursor=None
try:
    conn=pymysql.connect(host='211.103.136.244',port=7061,user='student',password='iHRM_student_2022',database='test_db',charset='utf8')
    cursor=conn.cursor()
    cursor.execute("select * from t_book where title='西游记'and pub_date='1986-01-01'")
    book= cursor.fetchone()
    if book is None:
        cursor.execute("insert into t_book(id,title,pub_date) values(5,'西游记','1986-01-01')")
        conn.commit()
    cursor.execute("select `read` from t_book where title='西游记'and pub_date='1986-01-01'")#一直cursor.fetchone得到read,其实是因为read使用的单引号而不是esc底下的反引号
    rea=cursor.fetchone()
    readnum=rea[0]+1
    print('rednum是好多',readnum)
    cursor.execute("UPDATE t_book set `comment`=50  where title='放弃Python入门到熟练' and pub_date='2022-12-06'" )  # 可以先dbwerver没问题才复制过来
    print('查看当前sql语句影响行数', conn.affected_rows())
    conn.commit()
except Exception as f:
    print('出现问题',str(f))
    conn.rollback()
finally:
    cursor.close()
    conn.close()
'''



cursor.execute("UPDATE t_book set read=%d  where title='西游记'"%(readnum[0]+1))#可以先dbwerver没问题才复制过来
print('查看当前sql语句影响行数',conn.affected_rows())#查看当前sql语句影响行数
#提交或回滚事物
Duplicate entry '2' for key 'PRIMARY说的是条目2重复
'''
#conn.commit()









