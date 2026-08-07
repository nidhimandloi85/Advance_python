import pymysql

def testread2():
    connection=pymysql.connect(host='localhost',port=3306,user='root',password='root',database='rays')
    cur=connection.cursor()
    sql="select * from student"
    cur.execute(sql)
    data=cur.fetchall()
    columnname=('id','name','marks')
    for x in data:
        print({columnname [i]:x[i] for i, _ in enumerate(x)})
    connection.commit()
    connection.close()
testread2()    