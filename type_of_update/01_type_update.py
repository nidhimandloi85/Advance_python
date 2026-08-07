import pymysql

def testupdate1():
    connection=pymysql.connect(host='localhost',port=3306,user='root',password='root',database='rays')
    cur=connection.cursor()
    sql="update student set name='ram' where id=4"
    cur.execute(sql)
    connection.commit()
    print("record update successfully")
testupdate1()