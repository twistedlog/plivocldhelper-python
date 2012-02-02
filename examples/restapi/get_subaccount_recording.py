import sys
import plivocldhelper


AUTH_ID = 'YOUR_AUTH_ID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'
API_URL = "http://api.plivo.com"



r = plivocldhelper.RestAPI(AUTH_ID, AUTH_TOKEN, url=API_URL)

print r.get_subaccount_recording('SAZDBMMGQ4NDNKOGQ1YZ', '20120112-052747_29a012e4-3cde-11e1-aac3-4040e97a2e59')
