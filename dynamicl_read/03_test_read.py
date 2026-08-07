import pymysql

def testRead3():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='rays')
    cur = connection.cursor()

    # sql = "select * from student"
    # sql = "select * from student where id = 1"
    # sql = "select * from student where name like 'a%'"
    sql = "select * from student where marks = 90"

    print("sql =",sql)
    cur.execute(sql)
    result=cur.fetchall()
    for i in result:
        print(i)
    #connection.commit()
    connection.close()
testRead3()

