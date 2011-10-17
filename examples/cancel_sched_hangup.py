#!/usr/bin/env python
import plivocldhelper
import sys


try:
    schedid = sys.argv[1]
except IndexError:
    print "Need SchedHangupId"
    sys.exit(1)

# Sid and AuthToken
SID = 'OGEzODhiNDRhYTM5MTU1MzE3MWU2MTY1ZDFhNDQyZjg'
AUTH_TOKEN = 'MWU4OTA1MzgyY2JmZjEyZmI4Y2NjN2RlNTdkMGM2ZGM'

# Create a REST object
plivo = plivocldhelper.REST(SID, AUTH_TOKEN)

params = {'SchedHangupId':schedid}

try:
    print plivo.cancel_scheduled_hangup(params)
except Exception, e:
    print e
