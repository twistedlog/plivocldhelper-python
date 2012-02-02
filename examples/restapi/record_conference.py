#!/usr/bin/env python
import plivocldhelper
import sys


try:
    conf = sys.argv[1]
except IndexError:
    print "ROOM"
    sys.exit(1)

# Sid and AuthToken
AUTH_ID = 'YOUR_AUTH_ID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'
URL = "http://api.plivo.com"

# Create a REST object
r = plivocldhelper.RestAPI(AUTH_ID, AUTH_TOKEN, url=URL)

print r.record_conference(conf)
