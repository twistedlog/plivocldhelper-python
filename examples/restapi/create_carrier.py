import sys
import plivocldhelper


AUTH_ID = 'YOUR_AUTH_ID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'

r = plivocldhelper.RestAPI(AUTH_ID, AUTH_TOKEN)
params = {'name':"Your carrier", 
          'address':"your.carrier.com"
         )
print r.create_carrier(params)
