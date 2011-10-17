#!/usr/bin/env python
import plivocldhelper
import sys

try:
    member_filter = sys.argv[1]
except IndexError:
    member_filter = ""
try:
    uuid_filter = sys.argv[2]
except IndexError:
    uuid_filter = ""
try:
    only_mute = sys.argv[3]
except IndexError:
    only_mute = 'false'
try:
    only_deaf = sys.argv[4]
except IndexError:
    only_deaf = 'false'

# Sid and AuthToken
SID = 'OGEzODhiNDRhYTM5MTU1MzE3MWU2MTY1ZDFhNDQyZjg'
AUTH_TOKEN = 'MWU4OTA1MzgyY2JmZjEyZmI4Y2NjN2RlNTdkMGM2ZGM'

# Create a REST object
plivo = plivocldhelper.REST(SID, AUTH_TOKEN)

params = {'MemberFilter':member_filter, 
          'CallUUIDFilter':uuid_filter, 'MutedFilter':only_mute, 'DeafFilter':only_deaf}


try:
    print plivo.conference_list(params)
except Exception, e:
    print e
