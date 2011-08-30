#!/usr/bin/env python
import plivohelper
import sys


try:
    calluuid = sys.argv[1]
    digits = sys.argv[2]
except IndexError:
    print "Need CallUUID Digits [Leg]"
    sys.exit(1)

try:
    leg = sys.argv[3]
except IndexError:
    leg = ""

# URL of the Plivo REST Service
REST_API_URL = 'http://127.0.0.1:8088'
API_VERSION = 'v0.1'

# Sid and AuthToken
SID = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
AUTH_TOKEN = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'

# Create a REST object
plivo = plivohelper.REST(REST_API_URL, SID, AUTH_TOKEN, API_VERSION)

#call_params = {'CallUUID':calluuid, 'Digits':digits, 'Leg':leg}
call_params = {'CallUUID':calluuid, 'Digits':digits, 'Leg':leg}

try:
    print plivo.send_digits(call_params)
except Exception, e:
    print e
