#!/usr/bin/env python
import plivocldhelper
import sys


try:
    schedid = sys.argv[1]
except IndexError:
    print "Need SchedPlayId"
    sys.exit(1)

# Sid and AuthToken
SID = 'MTFMMJMZNTRHYTEXMTVM'
AUTH_TOKEN = 'OGRmYTNkMjBkMWI3NTNiZWU3MTM2M2U0M2EwMjRm'

# Create a REST object
plivo = plivocldhelper.REST(SID, AUTH_TOKEN)

params = {'SchedPlayId':schedid}

try:
    print plivo.cancel_scheduled_play(params)
except Exception, e:
    print e
