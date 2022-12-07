import sys

import mysql.connector

def connect():
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='level4d')
    except:
        print("Error: ", sys.exc_info())
    finally:
        return conn

def insert(notebook):
    conn = None
    sql = """INSERT INTO notebooks VALUES(%s, %s, %s)"""
    values = (notebook.getNID(), notebook.getPages(), notebook.getPrice())
    result = False
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result =True
    except:
        print("Error: ", sys.exc_info())
    finally:
        del values
        del sql
        del conn
        return result

def all():
    sql = """SELECT * FROM notebooks"""
    records = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        print("Error: ", sys.exc_info())
    finally:
        del sql
        return records

def search(nid):
    sql = """SELECT * FROM notebooks WHERE nid=%s"""
    values = (nid, )
    record = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        record = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, conn
        return record

def edit(notebook):
    sql = """UPDATE notebooks set pages=%s, price=%s WHERE nid=%s"""
    values = (notebook.getPages(), notebook.getPrice(), notebook.getNID())
    result = False
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result = True
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values, sql
        return result


def delete(nid):
    sql = """DELETE FROM notebooks WHERE nid=%s"""
    values = (nid, )
    result = False
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result = True
    except:
        print("Error ", sys.exc_info())
    finally:
        del values, sql
        return result