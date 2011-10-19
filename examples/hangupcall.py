#!/usr/bin/env python
import plivocldhelper
import sys


try:
    call_uuid = sys.argv[1]
except IndexError:
    print "need CallUUID argument"
    sys.exit(1)


# Sid and AuthToken
SID = 'MTFMMJMZNTRHYTEXMTVM'
AUTH_TOKEN = 'OGRmYTNkMjBkMWI3NTNiZWU3MTM2M2U0M2EwMjRm'

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
