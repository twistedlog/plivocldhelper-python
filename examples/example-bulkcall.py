#!/usr/bin/env python
import plivohelper


# Sid and AuthToken
SID = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
AUTH_TOKEN = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'

# Create a REST object
plivo = plivohelper.REST(SID, AUTH_TOKEN, )

# Initiate a new outbound call to user/1000 using a HTTP POST
# All parameters for bulk calls shall be separated by a delimeter
call_params = {
    'Delimiter' : '>', # Delimter for the bulk list
    'From': '919191919191', # Caller Id
    'To' : '1001>1000', # User Numbers to Call separated by delimeter
    'AnswerUrl' : "http://127.0.0.1:5000/answered/",
    'HangupUrl' : "http://127.0.0.1:5000/hangup/",
    'RingUrl' : "http://127.0.0.1:5000/ringing/",
#    'TimeLimit' : '10>30',
#    'HangupOnRing': '0>0',
}

try:
    print plivo.bulk_call(call_params)
except Exception, e:
    print e
