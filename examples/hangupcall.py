#!/usr/bin/env python
import plivocldhelper
import sys


try:
    call_uuid = sys.argv[1]
except IndexError:
    print "need CallUUID argument"
    sys.exit(1)


# Sid and AuthToken
SID = 'OGEzODhiNDRhYTM5MTU1MzE3MWU2MTY1ZDFhNDQyZjg'
AUTH_TOKEN = 'MWU4OTA1MzgyY2JmZjEyZmI4Y2NjN2RlNTdkMGM2ZGM'

# Create a REST object
plivo = plivocldhelper.REST(SID, AUTH_TOKEN)

params = {
    'CallUUID' : call_uuid, # CallUUID for Hangup
}

# Perform a hangup on a Call
try:
    print plivo.hangup_call(params)
except Exception, e:
    print e
