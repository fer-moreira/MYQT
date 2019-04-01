import mysql.connector as mysql

def connect (host,port,user,passw,bfr):
    return mysql.connect (
        host        =   host,port        =   port,
        user        =   user,passwd      =   passw,
        buffered    =   bfr)
def databases (cursor):
    cursor.execute('show databases')
    return cursor.fetchall()
def tables (cursor):
    cursor.execute('show tables')
    return cursor.fetchall()  
def Set_Database (cursor,name):
    cursor.execute('use %s' %name)
def Database (cursor):
    cursor.execute("SELECT DATABASE()")
    fetch = cursor.fetchall()
    return fetch[0][0]
def  Get_Struct (cursor,table):
    cursor.execute('desc %s' %table)
    return cursor.fetchall()
def Get_Data (cursor,table):
    cursor.execute('select * from %s limit 1000 '%table)
    return cursor.fetchall()

"""
Connector Function

- host='.'
- port='1443'
- user=''
- password=''
- database=''
- use_unicode=True
- charset='UTF-8'
- auto-commit=False
- get-warnings=False
- raise_on_warnings=False
- connection_timeout=5
- buffered=True
- raw=False
- force_ipv6=False
- pool_name=''
- pool_size=500
- pool_reset_session=False
- use_pure=True
- unix_socket=False
- auth_plugin=''
- sql_mode=''
"""