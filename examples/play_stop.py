#!/usr/bin/env python
import plivocldhelper
import sys


try:
    calluuid = sys.argv[1]
except IndexError:
    print "Need CallUUID"
    sys.exit(1)

# Sid and AuthToken
SID = 'OGEzODhiNDRhYTM5MTU1MzE3MWU2MTY1ZDFhNDQyZjg'
AUTH_TOKEN = 'OGRmYTNkMjBkMWI3NTNiZWU3MTM2M2U0M2EwMjRm'

# Create a REST object
plivo = plivocldhelper.REST(SID, AUTH_TOKEN)

params = {'CallUUID':calluuid}

try:
    print plivo.play_stop(params)
except Exception, e:
    print e
