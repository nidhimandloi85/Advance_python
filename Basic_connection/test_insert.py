import pymysql

connection=pymysql.connect(host='localhost',port=3306,user='root',password='root',database='rays')
cur=connection.cursor()
sql="insert into  student values(7,'neha',90)"
cur.execute(sql)
connection.commit()
print("record inserted successfully")
