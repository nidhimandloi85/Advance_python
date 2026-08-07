import pymysql


def testinsert(data={}):
    id=data['id']
    name=data['name']
    marks=data['marks']
    connection=pymysql.connect(host='localhost',port=3306,user='root',password='root',database='rays')
    cur=connection.cursor()
    sql="insert into student values(%s,%s,%s)"
    data=(id,name,marks)
    cur.execute(sql,data)
    connection.commit()
    connection.close()
    print("record insert successfully")

testinsert({'id':12,'name':'aman','marks':23})

