#!/usr/bin/env python
import plivocldhelper
import sys


try:
    room = sys.argv[1]
    memberid = sys.argv[2]
    text = sys.argv[3]
except IndexError:
    print "Need ConferenceName, MemberID, Text args"
    sys.exit(1)

# Sid and AuthToken
SID = 'OGEzODhiNDRhYTM5MTU1MzE3MWU2MTY1ZDFhNDQyZjg'
AUTH_TOKEN = 'MWU4OTA1MzgyY2JmZjEyZmI4Y2NjN2RlNTdkMGM2ZGM'

# Create a REST object
plivo = plivocldhelper.REST(SID, AUTH_TOKEN)

params = {'ConferenceName':room, 'MemberID':memberid, 'Text':text}

try:
    print plivo.conference_speak(params)
except Exception, e:
    print e
