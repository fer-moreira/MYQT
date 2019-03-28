import mysql.connector as mysql

def connect (host,port,user,passw,bfred):
    mydb = mysql.connect(
        host        =   host,
        port        =   port,
        user        =   user,
        passwd      =   passw,
        buffered    =   bfred,
        auth_plugin =  'caching_sha2_password'
    )
    return mydb

def databases (cursor):
    cursor.execute('show databases')
    dbs = cursor.fetchall()
    return dbs

def tables (cursor):
    cursor.execute('show tables')
    tbs = cursor.fetchall()
    return tbs

def Set_Database (cursor,name):
    cursor.execute('use %s' %name)

def  Get_Struct (cursor,table):
    cursor.execute('desc %s' %table)
    res = cursor.fetchall()
    return res
def Get_Data (cursor,table):
    cursor.execute('select * from %s'%table)
    res = cursor.fetchall()
    return res