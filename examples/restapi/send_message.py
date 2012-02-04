import plivocldhelper

AUTH_ID = 'YOUR_AUTH_ID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'

r = plivocldhelper.RestAPI(AUTH_ID, AUTH_TOKEN)
params = {'src': '123777777778',
          'dst': '199999999999',
          'text': 'hello',
          'type': 'sms'
         }
print r.send_message(params)
