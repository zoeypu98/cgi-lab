import cgi, cgitb
form = cgi.FieldStorage
username = form.getvalue('username')
password = form.getvalue('password')

print("Content-type: text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>hello - Second Test CGI</title>")
print("</head>")
print("<body>")
print("<p><b>Username</b> %s <b>password</b> %s</p>" % (username, password))

print("</body>")
print("</html>")