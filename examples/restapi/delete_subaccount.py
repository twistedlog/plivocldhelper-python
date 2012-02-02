import sys
import plivocldhelper


AUTH_ID = 'YOUR_AUTH_ID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'
API_URL = "http://api.plivo.com"



r = plivocldhelper.RestAPI(AUTH_ID, AUTH_TOKEN, url=API_URL)

print r.delete_subaccount('SAMZLIYZIYNTE2ZDQ1MJ')
