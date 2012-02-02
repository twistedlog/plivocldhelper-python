#!/usr/bin/env python
import plivocldhelper
import sys


try:
    calluuid = sys.argv[1]
except IndexError:
    print "Need CallUUID"
    sys.exit(1)

# Sid and AuthToken
AUTH_ID = 'YOUR_AUTH_ID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'
API_URL = "http://api.plivo.com"



r = plivocldhelper.RestAPI(AUTH_ID, AUTH_TOKEN, url=API_URL)
print r.send_digits(calluuid, digits="1234567890")
