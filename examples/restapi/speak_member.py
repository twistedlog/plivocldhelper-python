#!/usr/bin/env python
import plivocldhelper
import sys


try:
    conf = sys.argv[1]
    member = sys.argv[2]
    text = sys.argv[3]
except IndexError:
    print "ROOM MEMBERID TEXT"
    sys.exit(1)

# Sid and AuthToken
AUTH_ID = 'YOUR_AUTH_ID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'
URL = "http://api.plivo.com"

# Create a REST object
r = plivocldhelper.RestAPI(AUTH_ID, AUTH_TOKEN, url=URL)

print r.speak_member(conf, member, text=text)
