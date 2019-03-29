import pymssql

def connect (server,user,passw):
    return pymssql.connect(server,user,passw)
def databases (cursor):
   cursor.execute("SELECT name FROM sys.databases")
   return cursor.fetchall()
def tables (cursor):
    cursor.execute("SELECT name FROM SYSOBJECTS WHERE xtype = 'U'")
    return cursor.fetchall()
def Set_Database (cursor,name):
    cursor.execute("USE %s"%name)
def Database (cursor):
   cursor.execute("SELECT DB_NAME()")
   fetch = cursor.fetchall()
   return fetch[0][0]
def Get_Struct (cursor,table):
    cursor.execute("sp_columns '{0}'".format(table))
    return cursor.fetchall()
def Get_Data (cursor,table):
    cursor.execute("select * from %s"%table)
    return cursor.fetchall()
    