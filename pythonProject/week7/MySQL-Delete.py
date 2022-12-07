# import ilbrary
import sys
import mysql.connector  #connect CRUD to mysql
sql = """DELETE FROM persons WHERE pid=1"""
try:
    # connect with database
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="level4d")
    #delte record
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    #close connection
    cursor.close()
    conn.close()
    print("Delete Record Successfully")
except:
    print("Error: ", sys.exc_info())