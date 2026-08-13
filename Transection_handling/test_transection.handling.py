import pymysql

connection=pymysql.connect(host='localhost',port=3306,user='root',password='root',database='rays')

try:
    connection.autocommit(False)
    cur=connection.cursor()
    sql1 = "insert into student values(6, 'raj',13)"
    sql2 = "insert into student values(16,'raj', 88)"
    sql3 = "insert into student values(5,'raj',  68)"

    cur.execute(sql1)
    cur.execute(sql2)
    cur.execute(sql3)
    connection.commit()
    print("Transaction committed successfully")
except Exception as e:
    connection.rollback()
    print("transection called back due to error:",e)
