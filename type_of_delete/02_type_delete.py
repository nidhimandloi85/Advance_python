import pymysql

def testdelete2():
    connection=pymysql.connect(host='localhost',port=3306,user='root',password='root',database='rays')
    cur=connection.cursor()
    sql="delete from student where id=%s"
    data=(4)
    cur.execute(sql,data)
    connection.commit()
    print("record delete successfully")
testdelete2()    