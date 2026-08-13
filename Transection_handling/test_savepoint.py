import pymysql
connection=pymysql.connect(host='localhost',port=3306,user='root',password='root',database='rays',autocommit=False)
cur=connection.cursor()
try:
     print("starting transection ")
     cur.execute("insert into student values(21,'ruchi',90)")

     print("creatinng savepoint sp1")
     cur.execute("savepoint sp1")
     try:
         cur.execute("insert into  student values(22,'bhumi,44)")
         print("creating savving point sp2")
         cur.execute("savepoint sp2")
     except Exception as e:
         print("error in secound insert, rolling back to savpoint sp1")
         cur.execute("rollback to savepoint sp1")
try:
        cur.execute("insert into student values(19, 'kabir',38)")
        print("Second insert successful.")
        print("Creating savepoint sp3...")
        cur.execute("savepoint sp3")
    except Exception as e:
        print("Error in third insert, rolling back to savepoint sp1...")
        cur.execute("rollback to savepoint sp1")
print("commit transection")
connection.commit()

#except Exception as e:
       # print("error in transection",e)
       # connection.rollback()
except Exception as e:
    print("Error in transaction:", e)
    connection.rollback()
