import pymssql

def connect (server,user,passw):
    msdb = pymssql.connect(server,user,passw)
    return msdb
def databases (cursor):
   cursor.execute("SELECT name FROM sys.databases")
   dbs = cursor.fetchall()
   return dbs
def tables (cursor):
    cursor.execute("SELECT name FROM SYSOBJECTS WHERE xtype = 'U'")
    tbs = cursor.fetchall()
    return tbs
def Set_Database (cursor,name):
    cursor.execute("USE %s"%name)

def Get_Struct (cursor,table):
    cursor.execute("sp_columns '{0}'".format(table))
    res = cursor.fetchall()
    return res
def Get_Data (cursor,table):
    cursor.execute("select * from %s"%table)
    res = cursor.fetchall()
    return res