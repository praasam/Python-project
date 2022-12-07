import mysql.connector
import sys
from customer import Customer
def saveCustomer(customerInfo):
    conn = None
    sql = """INSERT INTO customers VALUES (%s, %s, %s, %s, %s, %s)"""
    values = customerInfo.getCID(), customerInfo.getName(), customerInfo.getAddress(), customerInfo.getEmail(), customerInfo.getTelephoneNo(), customerInfo.getPayment()
    try:
        conn = mysql.connector.connect(host='localhost',port='3306',user='root',password='',database='testss' )
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        print("Save customer!")
    except:
        print("Error: ", sys.exc_info())
    finally:
        del values
        del sql
        del conn

def searchCustomer(tn):
    conn = None
    sql = """SELECT * FROM customers WHERE telephoneno=%s"""
    values = (tn,)
    customer = None
    try:
        conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='testss')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        driver = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error: ", sys.exc_info())
    finally:
        del values
        del sql
        del conn
        return customer