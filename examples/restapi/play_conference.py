#!/usr/bin/env python
import plivocldhelper
import sys


try:
    conf = sys.argv[1]
    member = sys.argv[2]
    url = sys.argv[3]
except IndexError:
    print "ROOM MEMBERID URL"
    sys.exit(1)

# Sid and AuthToken
AUTH_ID = 'YOUR_AUTH_ID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'
URL = "http://api.plivo.com"

# Create a REST object
r = plivocldhelper.RestAPI(AUTH_ID, AUTH_TOKEN, url=URL)

print r.play_conference(conf, member, url=url)
