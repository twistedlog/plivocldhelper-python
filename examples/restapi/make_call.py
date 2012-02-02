#!/usr/bin/env python
import plivocldhelper
import sys


try:
    phone = sys.argv[1]
except IndexError:
    print "Need Phone"
    sys.exit(1)

# Sid and AuthToken
AUTH_ID = 'YOUR_AUTH_ID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'
URL = "http://api.plivo.com"

# Create a REST object
plivo = plivocldhelper.RestAPI(AUTH_ID, AUTH_TOKEN, url=URL)

params = {'to': phone,
          'from': '122222222222',
          'answer_url': 'http://electric-snow-3852.herokuapp.com/response/speak/',
          'ring_url': 'http://electric-snow-3852.herokuapp.com/ringing/',
          'hangup_url': 'http://electric-snow-3852.herokuapp.com/hangup/',
          'delimiter': '<',
         }

try:
    print plivo.make_call(**params)
except Exception, e:
    print e
