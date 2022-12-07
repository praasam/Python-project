# install library to connect
# https://pypi.org/
# pip install mysql-connector-python

# connect with Database Server
import mysql.connector  # import library
import sys
try:
    conn = mysql.connector.connect(host='localhost',user='root',password='',database='level4d')  #connect with mysql server
    conn.close()    #connection close
    print("Connect with database server successfully ")
except:
    print("Error", sys.exc_info())