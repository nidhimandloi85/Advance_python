import pymysql

def testupdate2():
    connection = pymysql.connect(host="localhost", port=3306, user="root", password="root", database='rays')
    cur = connection.cursor()
    sql = "update student set name=%s where id=%s "
    data = ('ayushi',2)
    cur.execute(sql, data)
    connection.commit()
    connection.close()
    print("record update successfully")


testupdate2()
