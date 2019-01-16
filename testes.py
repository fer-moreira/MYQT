
schema = {
    'SELECT':'<p style="color:yellow;">SELECT</p>',
    'FROM':'<p style="color:yellow;">FROM</p>',
    'INNER':'<p style="color:yellow;">INNER</p>',
    'JOIN':'<p style="color:yellow;">JOIN</p>',
    'ON':'<p style="color:yellow;">ON</p>',
    'AND':'<p style="color:yellow;">AND</p>',
    'USE':'<p style="color:yellow;">USE</p>'
}

query = input("Enter Query: ")

words = query.split(" ")

finalQuery = ""
for w in words:
    if w in schema.keys():
        scWord = schema.get(w)
        finalQuery += "%s " %scWord
    else:
        finalQuery += "%s " %w

print(finalQuery)