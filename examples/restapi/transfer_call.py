import plivocldhelper

AUTH_ID = 'YOUR_AUTH_ID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'

r = plivocldhelper.RestAPI(AUTH_ID, AUTH_TOKEN)
print r.transfer_call({'call_uuid':'XXXX', 
                       'url':'http://mytransferurl.dom',
                       'method':'GET'
                     })
