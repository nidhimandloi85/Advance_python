import pymysql


def testread4(id,name,marks):
    connection=pymysql.connect(host='localhost',port=3306,user='root',password='root',database='rays')
    cur=connection.cursor()
    sql="select * from student"
    if id !=0:
         sql+= "where id =" + str(id)
    if name != '':
        sql += " where name like '" + name + "%'"
    if marks != 0:
        sql += " where marks = " + str(marks)
    print("sql =",sql)
    cur.execute(sql)
    result=cur.fetchall()
    for i in result:
       print(i)
    connection.commit()
    connection.close()
testread4(0,'',88)

