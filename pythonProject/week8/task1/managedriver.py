import mysql.connector
import sys
from driver import Driver
# def saveDriver(driverInfo):
#     conn = None
#     sql = """INSERT INTO driver VALUES (%s, %s, %s, %s, %s)"""
#     values = driverInfo.getDID(), driverInfo.getName(), driverInfo.getAddress(), driverInfo.getEmail(), driverInfo.getLicenseNo()
#     try:
#         conn = mysql.connector.connect(host='localhost',port='3306',user='root',password='',database='testss' )
#         cursor = conn.cursor()
#         cursor.execute(sql, values)
#         conn.commit()
#         cursor.close()
#         conn.close()
#         print("Save driver!")
#     except:
#         print("Error: ", sys.exc_info())
#     finally:
#         del values
#         del sql
#         del conn


# def searchDriver(ln):
#     conn = None
#     sql = """SELECT * FROM driver WHERE licenseno=%s"""
#     values = (ln,)
#     driver = None
#     try:
#         conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='testss')
#         cursor = conn.cursor()
#         cursor.execute(sql, values)
#         driver = cursor.fetchall()
#         cursor.close()
#         conn.close()
#     except:
#         print("Error: ", sys.exc_info())
#     finally:
#         del values
#         del sql
#         del conn
#         return driver

# def editDriver(driverInfo):
#     conn = None
#     sql = """UPDATE driver SET name=%s, address=%s, email=%s, licenseno=%s WHERE did=%s"""
#     values = ( driverInfo.getName(), driverInfo.getAddress(), driverInfo.getEmail(), driverInfo.getLicenseNo(), driverInfo.getDID())
#     result = False
#     try:
#         conn=mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='testss')
#         cursor=conn.cursor()
#         cursor.execute(sql,values)
#         conn.commit()
#         cursor.close()
#         conn.close()
#         result = True
#     except:
#         print("Error: ", sys.exc_info())
#     finally:
#         del values
#         del sql
#         del conn
#         return result



# def deleteDriver(did):
#     conn = None
#     sql = """DELETE FROM driver WHERE did=%s"""
#     values = (did, )
#     result = False
#     try:
#         conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='testss')
#         cursor = conn.cursor()
#         cursor.execute(sql, values)
#         conn.commit()
#         cursor.close()
#         conn.close()
#         result = True
#     except:
#         print("Error: ", sys.exc_info())
#     finally:
#         del values
#         del sql
#         del conn
#         return result

#
# def allDriver():
#     conn = None
#     sql = """SELECT * FROM driver"""
#     drivers = None
#     try:
#         conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='testss')
#         cursor = conn.cursor()
#         cursor.execute(sql)
#         drivers = cursor.fetchall()
#         cursor.close()
#         conn.close()
#     except:
#         print("Error: ", sys.exc_info())
#     finally:
#         del sql
#         del conn
#         return drivers


