#!/usr/bin/env python
import plivohelper
import sys


try:
    calluuid = sys.argv[1]
    direction = sys.argv[2]
except IndexError:
    print "Need CallUUID AudioDirection [PitchSemiTones] [PitchOctaves] [Pitch] [Rate] [Tempo]"
    sys.exit(1)

try:
    s = sys.argv[3]
except IndexError:
    s = ''
try:
    o = sys.argv[4]
except IndexError:
    o = ''
try:
    p = sys.argv[5]
except IndexError:
    p = ''
try:
    r = sys.argv[6]
except IndexError:
    r = ''
try:
    t = sys.argv[7]
except IndexError:
    t = ''

# URL of the Plivo REST Service
REST_API_URL = 'http://127.0.0.1:8088'
API_VERSION = 'v0.1'

# Sid and AuthToken
SID = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
AUTH_TOKEN = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'

# Create a REST object
plivo = plivohelper.REST(REST_API_URL, SID, AUTH_TOKEN, API_VERSION)

call_params = {'CallUUID':calluuid, 'AudioDirection':direction,
               'PitchSemiTones':s, 'PitchOctaves':o, 'Pitch':p,
               'Rate':r, 'Tempo':t}

try:
    print plivo.sound_touch(call_params)
except Exception, e:
    print e
