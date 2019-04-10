"""dsn

Create a new database connection.

The connection parameters can be specified as a string:

conn = psycopg2.connect("dbname=test user=postgres password=secret")
or using a set of keyword arguments:

conn = psycopg2.connect(database="test", user="postgres", password="secret")
Or as a mix of both. The basic connection parameters are:

dbname: the database name
database: the database name (only as keyword argument)
user: user name used to authenticate
password: password used to authenticate
host: database host address (defaults to UNIX socket if not provided)
port: connection port number (defaults to 5432 if not provided)
Using the connection_factory parameter a different class or connections factory can be specified. It should be a callable object taking a dsn argument.

Using the cursor_factory parameter, a new default cursor factory will be used by cursor().
"""

import psycopg2

def connect (_host,_port,_user,_pass):
    """ connect(hostname,port,username,password)"""
    return psycopg2.connect (dbname='postgres',host=_host,port=_port,user=_user,password=_pass)
def databases (cursor):
    cursor.execute('\list')
    return cursor.fetchall()
def tables (cursor):
    cursor.execute('/dt')
    return cursor.fetchall()  
def Set_Database (cursor,name):
    cursor.execute('/c %s' %name)
def Database (cursor):
    cursor.execute('SELECT current_database();')
    fetch = cursor.fetchall()
    return fetch[0][0]
def  Get_Struct (cursor,table):
    cursor.execute('/d+ %s' %table)
    return cursor.fetchall()
def Get_Data (cursor,table):
    cursor.execute('SELECT * FROM %s LIMIT 1000' %table)
    return cursor.fetchall()


