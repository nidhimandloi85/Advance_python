import pymysql

def testupdate3(marks,id):
    connection=pymysql.connect(host='localhost',port=3306,user='root',password='root',database='rays')
    cur=connection.cursor()
    sql="update student set marks=%s where id=%s"
    data=(marks,id)
    cur.execute(sql,data)
    connection.commit()
    print("record update successfully")

testupdate3(90,4)
