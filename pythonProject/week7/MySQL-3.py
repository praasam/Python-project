import mysql.connector
import sys

def insertRecord(userInfo):
    conn =None
    sql = """INSERT INTO users values (%s, %s, %s, %s, %s, %s"""
    try:
        conn=mysql.connector.connect(host='localhost', user='root', password='', port='3306', database='level4d')
        cursor=conn.cursor()
        cursor.execute(sql, userInfo)
        conn.commit()
        cursor.close()
        conn.close()
        print("user inserted")
    except:
        print("Error: ", sys.exc_info())
    finally:
        del sql
        del conn

def loginUser(userInfo): #email, password
    conn=None
    sql="""SELECT * FROM users WHERE email=%s and password=%s"""
    try:
        conn=mysql.connector.connect(host='localhost', user='root', password='', port='3306', database='level4d')
        cursor=conn.cursor()
        cursor.execute(sql, userInfo)
        user=cursor.fetchone()
        if user!=None:
            print('Welcome', user[1])
        else:
            print("User not found")
        cursor.close()
        conn.close()
    except:
        print("Error:", sys.exc_info())
    finally:
        del sql
        del conn

#test
# userInfo=(1, 'prasamsha', 'thecho', 'mahjprasam@gmail.com','12345','9878909878')
# insertRecord(userInfo)
userInfo=('mahjprasam@gmail.com', '12345')
loginUser(userInfo)