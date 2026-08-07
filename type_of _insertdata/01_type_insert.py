import pymysql


connection=pymysql.connect(host='localhost',port=3306,user='root',password='root',database='rays')
cur=connection.cursor()

sql="insert into student values(8,'arpita',57)"
cur.execute(sql)
connection.commit()
print("record insert successfully")
