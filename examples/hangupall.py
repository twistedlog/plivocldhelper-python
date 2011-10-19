#!/usr/bin/env python
import plivocldhelper
import sys


# Sid and AuthToken
SID = 'OGEzODhiNDRhYTM5MTU1MzE3MWU2MTY1ZDFhNDQyZjg'
AUTH_TOKEN = 'OGRmYTNkMjBkMWI3NTNiZWU3MTM2M2U0M2EwMjRm'

# Create a REST object
plivo = plivocldhelper.REST(SID, AUTH_TOKEN)

# Perform a hangup on a Call
try:
    print plivo.hangup_all_calls()
except Exception, e:
    print e
