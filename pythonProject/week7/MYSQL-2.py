import sys
import mysql.connector

# def insertRecord():
#     try:
#         sql="""INSERT INTO students VALUES(%s, %s, %s, %s)"""
#         values=[2,'Aasma', 78, 78]
#         conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
#         cursor=conn.cursor()
#         cursor.execute(sql, values)
#         conn.commit()
#         cursor.close()
#         conn.close()
#         print("Record Inserted Successfully")
#     except:
#         print("Error: ", sys.exc_info())

# def searchRecord():
#     try:
#         sid=(1,)
#         sql="""SELECT * FROM students WHERE sid=%s"""
#         conn=mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
#         cursor=conn.cursor()
#         cursor.execute(sql, sid)
#         record=cursor.fetchone()
#         print(record)
#         cursor.close()
#         conn.close()
#     except:
#         print("Error: ", sys.exc_info())

# def displayAll():
#     try:
#         sql="SELECT * FROM students"
#         conn=mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
#         cursor=conn.cursor()
#         cursor.execute(sql)
#         records=cursor.fetchall()
#         print(records)
#         cursor.close()
#         conn.close()
#     except:
#         print("Error: ", sys.exc_info())
#
# def updateRecord():
#     try:
#         values=('Deeshri', 98, 92, 1)
#         sql="""UPDATE students set name=%s, isd=%s, fcs=%s WHERE sid=%s"""
#         conn=mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
#         cursor=conn.cursor()
#         cursor.execute(sql,values)
#         conn.commit()
#         cursor.close()
#         conn.close()
#         print("Record Updated Successfully")
#     except:
#         print("Error: ", sys.exc_info())

def deleteRecord():
    try:
        sid=(1, )
        sql="DELETE FROM students WHERE sid=%s"
        conn=mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
        cursor=conn.cursor()
        cursor.execute(sql,sid)
        conn.commit()
        cursor.close()
        conn.close()
        print("Record Deleted Successfully")
    except:
        print("Error: ", sys.exc_info())



 #test
# insertRecord()
# # searchRecord()
# displayAll()
# updateRecord()
deleteRecord()