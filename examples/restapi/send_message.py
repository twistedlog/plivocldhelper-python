#!/usr/bin/env python
import plivocldhelper

# Sid and AuthToken
AUTH_ID = 'YOUR_AUTH_ID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'
URL = "http://api.plivo.com"

# Create a REST object
r = plivocldhelper.RestAPI(AUTH_ID, AUTH_TOKEN, url=URL)

params = {'src': '123777777778',
          'dst': '199999999999',
          'text': 'hello',
          'type': 'sms'
         }

print r.send_message(**params)
