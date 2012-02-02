#!/usr/bin/env python
import plivocldhelper
import sys


try:
    calluuid = sys.argv[1]
    sound_url = sys.argv[2]
except IndexError:
    print "Need CallUUID URL"
    sys.exit(1)

# Sid and AuthToken
AUTH_ID = 'YOUR_AUTH_ID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'
API_URL = "http://api.plivo.com"



r = plivocldhelper.RestAPI(AUTH_ID, AUTH_TOKEN, url=API_URL)
print r.play(calluuid, urls=sound_url)
