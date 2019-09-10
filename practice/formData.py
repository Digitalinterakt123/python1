import cgi,cgitb

form = cgi.FieldStorage()

first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')

print('first_name: ',first_name, ',', 'last_name: ', last_name)