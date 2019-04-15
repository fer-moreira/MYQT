"""
Create a new database connection.

The connection parameters can be specified as a string:

conn = psycopg2.connect("dbname=test user=postgres password=secret")
or using a set of keyword arguments:

- host='0.0.0.0'
- hostaddr='0.0.0.0'
- port=5432
- dbname=''
- user=''
- password=''
- passfile=~/.pgpass, or %APPDATA%\postgresql\pgpass.conf
- connect_timeout=5
- application_name='Application Name'

"""

import psycopg2

def connect (_database,_host,_port,_user,_pass):
    """ connect(hostname,port,username,password)"""
    return psycopg2.connect (dbname=_database,host=_host,port=_port,user=_user,password=_pass)
def databases (cursor):
    cursor.execute("SELECT datname FROM pg_database WHERE datistemplate = false")
    return cursor.fetchall()
def tables (cursor):
    cursor.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'""")
    return cursor.fetchall()  
def Set_Database (mydb,name):
    print("error")
def Database (cursor):
    cursor.execute("SELECT current_database()")
    fetch = cursor.fetchall()
    return fetch[0][0]
def  Get_Struct (cursor,table):
    cursor.execute(""" select * from INFORMATION_SCHEMA.COLUMNS where table_name = '%s' """ %table)
    return cursor.fetchall()
    print("Get_Struct ")
def Get_Data (cursor,table):
    cursor.execute("SELECT * FROM %s LIMIT 1000" %table)
    return cursor.fetchall()


