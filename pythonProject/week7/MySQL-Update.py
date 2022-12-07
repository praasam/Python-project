# import library
import sys
import mysql.connector
sql = """UPDATE persons set name='Aasma Subba', address='JHAPA' WHERE pid=1"""
try:
    # connect with database
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="level4d")

    # update record
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

    # close connection
    cursor.close()
    conn.close()
    print("Update record successfully")
except:
    print("Error: ",sys.exc_info())
