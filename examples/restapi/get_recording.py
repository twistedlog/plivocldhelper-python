import sys
import plivocldhelper


AUTH_ID = 'YOUR_AUTH_ID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'
API_URL = "http://api.plivo.com"


r = plivocldhelper.RestAPI(AUTH_ID, AUTH_TOKEN, url=API_URL)

print r.get_recording('20120112-091620_173743c8-3cfe-11e1-aac3-4040e97a2e59')
