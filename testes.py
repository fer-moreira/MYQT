
schema = {
    'SELECT':'<p style="color:red;">SELECT</p>',
    'FROM':'<p style="color:yellow;">FROM</p>',
    'INNER':'<p style="color:blue;">INNER</p>',
    'JOIN':'<p style="color:dark;">JOIN</p>',
    'ON':'<p style="color:green;">ON</p>',
    'AND':'<p style="color:blue;">AND</p>',
    'USE':'<p style="color:cyan;">USE</p>'
}

words = query.split(" ")

finalQuery = ""
for w in words:
    if w in schema.keys():
        scWord = schema.get(w)
        finalQuery += "%s " %scWord
    else:
        finalQuery += "%s " %w