#!/usr/bin/env python
import plivocldhelper
import sys

try:
    phone = sys.argv[1]
except:
    print "Need phone number to call"

# Sid and AuthToken
SID = 'OGEzODhiNDRhYTM5MTU1MzE3MWU2MTY1ZDFhNDQyZjg'
AUTH_TOKEN = 'MWU4OTA1MzgyY2JmZjEyZmI4Y2NjN2RlNTdkMGM2ZGM'

# Create a REST object
plivo = plivocldhelper.REST(SID, AUTH_TOKEN)

params = {
    'From': '919191919191', # Caller Id
    'To' : phone, # User Number to Call
    'AnswerUrl' : "http://radiant-leaf-8294.herokuapp.com/response4/",
    'HangupUrl' : "http://radiant-leaf-8294.herokuapp.com/response4/",
    'RingUrl' : "http://radiant-leaf-8294.herokuapp.com/response4/",
}

try:
    result = plivo.call(params)
    print result
except Exception, e:
    print e
    raise

