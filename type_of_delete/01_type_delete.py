import pymysql


def testdelete1():
    connection=pymysql.connect(host='localhost',port=3306,user='root',password='root',database='rays')
    cur=connection.cursor()
    sql="delete from student where id=2"
    cur.execute(sql)
    connection.commit()
    print("record delete successfully")
testdelete1()    