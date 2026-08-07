import pymysql

def testdelete3(id):
    connection=pymysql.connect(host='localhost',port=3306,user='root',password='root',database='rays')
    cur=connection.cursor()
    sql="delete from student where id =%s"
    data=(id,)
    cur.execute(sql,data)
    connection.commit()
    print("record delete successfully")
testdelete3(5)
