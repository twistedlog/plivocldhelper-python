import plivocldhelper

AUTH_ID = 'YOUR_AUTH_ID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'

r = plivocldhelper.RestAPI(AUTH_ID, AUTH_TOKEN)
print r.modify_subaccount({'subauth_id':'SAMZLIYZIYNTE2ZDQ1MJ', 'enabled':True})
