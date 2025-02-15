#!/usr/bin/env python3
import os, json
from posix import environ
print("Content-type: text/html\r\n\r\n")
print("<title>Test CGI</title>")
print("<p>Hello World!</p>")

print(os.environ)
json_object = json.dumps(dict(os.environ), indent=4)
print(json_object)

for param in os.environ.keys():
    if(param=="QUERY_STRING"):
        print(f"<em>{param}</em> = {os.environ[param]}</li>")
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))

for param in os.environ.keys():
    if(param=="HTTP_USER_AGENT"):
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))