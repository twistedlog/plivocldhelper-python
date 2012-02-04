import plivocldhelper


AUTH_ID = 'YOUR_AUTH_ID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'

r = plivocldhelper.RestAPI(AUTH_ID, AUTH_TOKEN)
params = {'subauth_id':'SAZDBMMGQ4NDNKOGQ1YZ',
          'username':'subtest', 
          'domain':'subdom.plivo.com', 
          'password':'sub'
         }
print r.create_subaccount_endpoint(params)
