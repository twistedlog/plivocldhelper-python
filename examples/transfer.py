#!/usr/bin/env python
import plivocldhelper
import sys


# URL of the Plivo
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
    'Url' : "http://radiant-leaf-8294.herokuapp.com/response4/",
    'CallUUID' : call_uuid, # CallUUID to transfer
}

try:
    print plivo.transfer_call(params)
except Exception, e:
    print e
