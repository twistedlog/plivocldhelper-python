#!/usr/bin/env python
import plivocldhelper
import sys


try:
    room = sys.argv[1]
    memberid = sys.argv[2]
except IndexError:
    print "Need ConferenceName and MemberID args"
    sys.exit(1)

# Sid and AuthToken
SID = 'OGEzODhiNDRhYTM5MTU1MzE3MWU2MTY1ZDFhNDQyZjg'
AUTH_TOKEN = 'OGRmYTNkMjBkMWI3NTNiZWU3MTM2M2U0M2EwMjRm'

# Create a REST object
plivo = plivocldhelper.REST(SID, AUTH_TOKEN)

params = {'ConferenceName':room, 'MemberID':memberid}

try:
    print plivo.conference_undeaf(params)
except Exception, e:
    print e
