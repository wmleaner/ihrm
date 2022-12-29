import pymysql
conn=None
cursor=None
try:
    conn=pymysql.connect(host='211.103.136.244',port=7061,user='student',password='iHRM_student_2022',database='test_db',charset='utf8')
    cursor=conn.cursor()
    cursor.execute("INSERT into test_db.t_book(title,pub_date,`read`,comment) values('放弃Python入门到熟练','2022-12-06',50,0)")#可以先dbwerver没问题才复制过来
    print('查看当前sql语句影响行数',conn.affected_rows())#查看当前sql语句影响行数
    '''提交或回滚事物
    Duplicate entry '2' for key 'PRIMARY说的是条目2重复
    '''
    conn.commit()
except Exception as f:
    print('出现问题',str(f))
    conn.rollback()
finally:
    cursor.close()
    conn.close()
