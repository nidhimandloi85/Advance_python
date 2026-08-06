import pymysql

connection=pymysql.connect(host='localhost',port=3306,user='root',password='root',database='rays')
cur=connection.cursor()
sql="update student set  name='aastha' where id=2"
cur.execute(sql)
connection.commit()
print("record update successfully")