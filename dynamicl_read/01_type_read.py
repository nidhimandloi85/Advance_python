import pymysql

def testread1():
    connection=pymysql.connect(host='localhost',port=3306,user='root',password='root',database='rays')
    cur=connection.cursor()
    sql="select * from student"
    cur.execute(sql)
    data=cur.fetchall()
    for i in data:
        print(i)
    connection.commit()
    connection.close()
    print("data read successfully")



testread1()