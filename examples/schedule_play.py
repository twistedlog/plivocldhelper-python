#!/usr/bin/env python
import plivocldhelper
import sys


try:
    calluuid = sys.argv[1]
    sounds = sys.argv[2]
    time = sys.argv[3]
except IndexError:
    print "Need CallUUID Sounds Time args"
    sys.exit(1)

# Sid and AuthToken
SID = 'OGEzODhiNDRhYTM5MTU1MzE3MWU2MTY1ZDFhNDQyZjg'
AUTH_TOKEN = 'MWU4OTA1MzgyY2JmZjEyZmI4Y2NjN2RlNTdkMGM2ZGM'

# Create a REST object
plivo = plivocldhelper.REST(SID, AUTH_TOKEN)

params = {'CallUUID':calluuid, 'Sounds':sounds, 'Time':time}

try:
    print plivo.schedule_play(params)
except Exception, e:
    print e
