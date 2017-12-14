#!/usr/bin/python
#Send simple HTTP requests
import requests

def headers(uri):
    with requests.get(uri) as r:
        return  "The HTTP headers details: %s \n status_code: %s"  % (r.headers , r.status_code)
#api Check
uri = 'url'
#output result
f = open('filename','w')
f.write(headers(uri))
f.close()
 
