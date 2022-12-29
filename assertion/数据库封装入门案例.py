import pymysql
#连接数据库
conn=pymysql.connect(host="211.103.136.244",port=7061,user="student",password="iHRM_student_2022",database="test_db",charset="utf8")
#创建游标
cursor=conn.cursor()
#执行语句
cursor.execute('select `read` from t_book where id=5')
#获取结果

ret=cursor.fetchone()
print(ret[0])
#关闭游标和sql连接
cursor.close()
conn.close()
