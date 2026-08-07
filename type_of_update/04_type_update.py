import pymysql



def testupdate4(data):
    id=data['id']
    name=data['name']
    connection=pymysql.connect(host='localhost',port=3306,user='root',password='root',database='rays')
    cur=connection.cursor()
    sql="update student set name=%s where id =%s"
    data=(name,id)
    cur.execute(sql,data)
    connection.commit()
    print("record update successfully")
data={}
data['id']=7
data['name']="ayushi"
testupdate4(data)

