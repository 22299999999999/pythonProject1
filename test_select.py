import pymysql

db = pymysql.connect(host='182.92.129.158',
                     user='tmp',
                     password='ceshiren.com',
                     database='tmp123',
                     cursorclass=pymysql.cursors.DictCursor)


def test_select():
    with db.cursor() as cursor:
        # Create a new record
        sql = "show tables;"
        cursor.execute(sql)
        print(sql)
        print(cursor.fetchall())
