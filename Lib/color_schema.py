"""MYQT.color_schema highlight syntax module"""

purplePat   = '<span style="color:rgb(195,114,195);">{0}</span>'
grayPat     = '<span style="color:rgb(105,105,105);">{0}</span>'

redPat    = '<span style="color:rgb(200, 0, 0);">{0}</span>'
greenPat    = '<span style="color:rgb(143,195,45);">{0}</span>'
bluePat     = '<span style="color:rgb(96,117,255);">{0}</span>'


schema = {
    '(': grayPat,
    ')': grayPat,
    '=': grayPat,

    'select'    : grayPat,
    'from'      : grayPat,
    'inner'     : grayPat,
    'join'      : grayPat,
    'on'        : grayPat,
    'create'    : grayPat,
    'table'     : grayPat,
    'show'      : grayPat,
    'update'    : grayPat,
    'key'       : grayPat,
    'desc'      : grayPat,
    'as'        : grayPat,
    'reference' : grayPat,
    'foreign'   : grayPat,
    'use'       : grayPat,
    'limit'     : grayPat,
    'references': grayPat,
    'and'       : grayPat,

    'collate'       : grayPat,
    'smallint'      : grayPat,
    'primary'       : grayPat,
    'not'           : grayPat,
    'null'          : grayPat,
    'auto_increment': grayPat,
    'order'         : grayPat,
    'by'            : grayPat,
    'group'         : grayPat,
    'asc'           : grayPat,
    'cascade'       : grayPat,
    'constraint'    : grayPat,

    'foreign'   : bluePat,
    'key'       : bluePat,
    'primary'   : bluePat,

    '*'         : purplePat,
    ','         : purplePat,

    'smallint'  : purplePat,
    'unsigned'  : purplePat,

    'innodb'    : purplePat,
    'varchar'   : purplePat,
    'utf8'      : purplePat,
    'tinyint'   : purplePat,
    'default'   : purplePat,

    '(' : redPat,
    ')' : redPat,

    'charset'   : '<br></br>%s' % bluePat,
    'engine'    : '<br></br>%s' % bluePat
}