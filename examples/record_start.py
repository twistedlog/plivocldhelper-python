#!/usr/bin/env python
import plivocldhelper
import sys


try:
    calluuid = sys.argv[1]
except IndexError:
    print "Need CallUUID"
    sys.exit(1)
try:
    timelimit = sys.argv[2]
except IndexError:
    timelimit = ''

# Sid and AuthToken
SID = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
AUTH_TOKEN = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'

# Create a REST object
plivo = plivocldhelper.REST(SID, AUTH_TOKEN)

params = {'CallUUID':calluuid, 'TimeLimit':timelimit}

try:
    print plivo.record_start(params)
except Exception, e:
    print e
