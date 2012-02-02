import sys
import plivocldhelper


AUTH_ID = 'YOUR_AUTH_ID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'
API_URL = "http://api.plivo.com"



r = plivocldhelper.RestAPI(AUTH_ID, AUTH_TOKEN, url=API_URL)

print r.create_carrier_routing(description="Voxbeam FR route", 
                               carrier_id="28235784856925", 
                               digits="33", priority=1)
