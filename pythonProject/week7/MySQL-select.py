#import library
import sys
import mysql.connector
sql = """SELECT * FROM persons"""
try:
    #connect
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="level4d")
    cursor = conn.cursor()
    cursor.execute(sql)
    records = cursor.fetchall()
    print(records)
    # close
    conn.close()
    print("Records retrieve successfully")
except:
    print("Error: ", sys.exc_info()) #display error message


