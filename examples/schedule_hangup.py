#!/usr/bin/env python
import plivocldhelper
import sys


try:
    calluuid = sys.argv[1]
    time = sys.argv[2]
except IndexError:
    print "Need CallUUID Time args"
    sys.exit(1)

# Sid and AuthToken
SID = 'MTFMMJMZNTRHYTEXMTVM'
AUTH_TOKEN = 'OGRmYTNkMjBkMWI3NTNiZWU3MTM2M2U0M2EwMjRm'

# Create a REST object
plivo = plivocldhelper.REST(SID, AUTH_TOKEN)

params = {'CallUUID':calluuid, 'Time':time}

try:
    print plivo.schedule_hangup(params)
except Exception, e:
    print e
