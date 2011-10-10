#!/usr/bin/env python
import plivocldhelper
from time import sleep

# Sid and AuthToken
SID = 'OGEzODhiNDRhYTM5MTU1MzE3MWU2MTY1ZDFhNDQyZjg'
AUTH_TOKEN = 'MWU4OTA1MzgyY2JmZjEyZmI4Y2NjN2RlNTdkMGM2ZGM'

# Create a REST object
plivo = plivocldhelper.REST(SID, AUTH_TOKEN)

# Initiate a new outbound call to user/1000 using a HTTP POST
call_params = {
    'From': '919191919191', # Caller Id
    'To' : '919611055344', # User Number to Call
    'AnswerUrl' : "http://radiant-leaf-8294.herokuapp.com/response4/",
    'HangupUrl' : "http://radiant-leaf-8294.herokuapp.com/response4/",
    'RingUrl' : "http://radiant-leaf-8294.herokuapp.com/response4/",
#    'TimeLimit' : '10',
#    'HangupOnRing': '0',
}

request_uuid = ""

#Perform the Call on the Rest API
try:
    result = plivo.call(call_params)
    print result
except Exception, e:
    print e
    raise


if False:
    sleep(10)
    # Hangup a call using a HTTP POST
    hangup_call_params = {
        'RequestUUID' : request_uuid.strip(), # Request UUID to hangup call
    }

    #Perform the Call on the Rest API
    try:
        print plivo.hangup_call(hangup_call_params)
    except Exception, e:
        print e
