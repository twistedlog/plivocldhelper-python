#!/usr/bin/env python
import plivocldcldhelper
import sys


try:
    calluuid = sys.argv[1]
    sounds = sys.argv[2]
except IndexError:
    print "Need CallUUID Sounds [Legs] [Mix]"
    sys.exit(1)

try:
    legs = sys.argv[3]
except IndexError:
    legs = ""
try:
    mix = sys.argv[4]
except IndexError:
    mix = 'true'

# Sid and AuthToken
SID = 'OGEzODhiNDRhYTM5MTU1MzE3MWU2MTY1ZDFhNDQyZjg'
AUTH_TOKEN = 'OGRmYTNkMjBkMWI3NTNiZWU3MTM2M2U0M2EwMjRm'

# Create a REST object
plivo = plivocldhelper.REST(SID, AUTH_TOKEN)

params = {'CallUUID':calluuid, 'Sounds':sounds, 'Legs':legs, 'Length':3600, 'Mix':mix}

try:
    print plivo.play(params)
except Exception, e:
    print e
