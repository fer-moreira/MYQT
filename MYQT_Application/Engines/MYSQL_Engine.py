import mysql.connector as mysql

def connect (host,port,user,passw,bfred):
    return mysql.connect (
        host        =   host,
        port        =   port,
        user        =   user,
        passwd      =   passw,
        buffered    =   bfred,
        auth_plugin =  'caching_sha2_password')
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
    cursor.execute('select * from %s'%table)
    return cursor.fetchall()