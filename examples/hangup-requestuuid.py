#!/usr/bin/env python
import plivocldhelper
import sys


try:
    request_uuid = sys.argv[1]
except IndexError:
    print "need RequestUUID argument"
    sys.exit(1)


# Sid and AuthToken
SID = 'OGEzODhiNDRhYTM5MTU1MzE3MWU2MTY1ZDFhNDQyZjg'
AUTH_TOKEN = 'MWU4OTA1MzgyY2JmZjEyZmI4Y2NjN2RlNTdkMGM2ZGM'

# Create a REST object
plivo = plivocldhelper.REST(SID, AUTH_TOKEN)

params = {
    'RequestUUID' : resuest_uuid,
}

# Perform a hangup on a Call
try:
    print plivo.hangup_call(params)
except Exception, e:
    print e
