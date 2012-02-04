import plivocldhelper

AUTH_ID = 'YOUR_AUTH_ID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'

r = plivocldhelper.RestAPI(AUTH_ID, AUTH_TOKEN)
params = {'to': '16789900000<16778999000',
          'from': '122222222222',
          'answer_url': 'http://myanswerurl.dom/',
          'ring_url': 'http://myringurl.dom/',
          'hangup_url': 'http://hangupurl.dom',
          'delimiter':'<'
         }
print r.make_call(params)
