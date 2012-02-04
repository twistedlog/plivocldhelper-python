import sys
import plivocldhelper


AUTH_ID = 'YOUR_AUTH_ID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'

r = plivocldhelper.RestAPI(AUTH_ID, AUTH_TOKEN)
params = {'description':"Carrier route", 
          'carrier_id':"28235784856925", 
          'digits':"33", 
          'priority':1
         }
print r.create_carrier_routing(params)
