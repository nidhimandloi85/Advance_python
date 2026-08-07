import pymysql

def testinsert():
     connection=pymysql.connect(host="localhost",port=3306,user="root",password="root",database='rays')
     cur=connection.cursor()
     sql="insert into student values(%s,%s,%s)"
     data=(9,'buddy',67)
     cur.execute(sql,data)
     connection.commit()
     connection.close()
     print("record insert successfully")

testinsert()
