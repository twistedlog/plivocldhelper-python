import plivocldhelper

AUTH_ID = 'YOUR_AUTH_ID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'

r = plivocldhelper.RestAPI(AUTH_ID, AUTH_TOKEN)
print r.get_subaccount_number({'subauth_id':'SAZDBMMGQ4NDNKOGQ1YZ', 'number':'1677790550'})
