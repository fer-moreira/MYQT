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
    cursor.execute("select top(1000) * from %s"%table)
    return cursor.fetchall()
    
"""
Connector Functions

- database=''
- server='.' 
- user=None 
- password=None
- host=''
- port='1433' 
- timeout=0
- login_timeout=60
- charset='UTF-8' 
- as_dict=False
- appname=None
- conn_properties=None
- autocommit=False
- tds_version=None
"""