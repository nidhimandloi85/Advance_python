import pymysql
connection=pymysql.connect(host="localhost",port=3306,user='root',password='root',database='rays')
cur=connection.cursor()
sql="delete from student where id=3"
cur.execute(sql)
connection.commit()
print("Record delete successfully")