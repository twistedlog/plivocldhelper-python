import plivocldhelper

AUTH_ID = 'YOUR_AUTH_ID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'

r = plivocldhelper.RestAPI(AUTH_ID, AUTH_TOKEN)
params = {'to': '17897899009',
          'from': '122222222222',
          'answer_url': 'http://myanswerurl.dom/',
          'ring_url': 'http://myringurl.dom/',
          'hangup_url': 'http://hangupurl.dom'
         }
print r.make_call(params)
