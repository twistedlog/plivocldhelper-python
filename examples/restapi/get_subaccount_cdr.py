import plivocldhelper

AUTH_ID = 'YOUR_AUTH_ID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'

r = plivocldhelper.RestAPI(AUTH_ID, AUTH_TOKEN)
print r.get_subaccount_cdr({'subauth_id':'SAZDBMMGQ4NDNKOGQ1YZ', 'record_id':'XXXX'})
