import pymysql

connection=pymysql.connect(host='localhost', port=3306 ,user='root',password='root',database='rays')
connection.autocommit(True)
cur=connection.cursor()
sql1="insert into student values(20,'saloni',23)"
sql2="insert into student values(19,'kanya',89)"
sql3="insert into student values(18,'pari',47)"
cur.execute(sql1)
cur.execute(sql2)
cur.execute(sql3)
connection.close()
print("data get successfully")