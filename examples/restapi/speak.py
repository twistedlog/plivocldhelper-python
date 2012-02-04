import plivocldhelper

AUTH_ID = 'YOUR_AUTH_ID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'

r = plivocldhelper.RestAPI(AUTH_ID, AUTH_TOKEN)
print r.speak({'call_uuid':'XXXX', 
               'text':"hello how are you ?",
               'voice':'WOMAN',
               'language':'en-US'
             })
