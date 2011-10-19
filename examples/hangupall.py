#!/usr/bin/env python
import plivocldhelper
import sys


# Sid and AuthToken
SID = 'MTFMMJMZNTRHYTEXMTVM'
AUTH_TOKEN = 'OGRmYTNkMjBkMWI3NTNiZWU3MTM2M2U0M2EwMjRm'

# Create a REST object
plivo = plivocldhelper.REST(SID, AUTH_TOKEN)

# Perform a hangup on a Call
try:
    print plivo.hangup_all_calls()
except Exception, e:
    print e
