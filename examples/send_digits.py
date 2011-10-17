#!/usr/bin/env python
import plivocldhelper
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

# Sid and AuthToken
SID = 'OGEzODhiNDRhYTM5MTU1MzE3MWU2MTY1ZDFhNDQyZjg'
AUTH_TOKEN = 'MWU4OTA1MzgyY2JmZjEyZmI4Y2NjN2RlNTdkMGM2ZGM'

# Create a REST object
plivo = plivocldhelper.REST(SID, AUTH_TOKEN)

params = {'CallUUID':calluuid, 'Digits':digits, 'Leg':leg}

try:
    print plivo.send_digits(params)
except Exception, e:
    print e
