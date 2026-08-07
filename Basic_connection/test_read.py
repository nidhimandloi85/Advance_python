import pymysql


connection=pymysql.connect(host='localhost',port=3306,user='root',password='root',database='rays')
cur=connection.cursor()
sql="select * from student"
cur.execute(sql)
result=cur.fetchall()
print(result)
for data in result:
    print(data[0],data[1],data[2])
connection.close()
print("data read successfully")
