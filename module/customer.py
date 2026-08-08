import pymysql

def testcustomer(data={}):
    customerid = data['customerid']
    customername = data['customername']
    email = data['email']
    phonenumber = data['phonenumber']
    address = data['address']

    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root',
        database='testdemo'
    )

    cur = connection.cursor()

    sql = "insert into customer values(%s,%s,%s,%s,%s)"

    data = (customerid, customername, email, phonenumber, address)

    cur.execute(sql, data)
    connection.commit()

    connection.close()

    print("record insert successfully")


testcustomer({
    'customerid': 105,
    'customername': 'nidhi',
    'email': 'nidhi@gmail.com',
    'phonenumber': '4567382910',
    'address': 'indore'
})
