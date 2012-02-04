import plivocldhelper

AUTH_ID = 'YOUR_AUTH_ID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'

r = plivocldhelper.RestAPI(AUTH_ID, AUTH_TOKEN)
print r.modify_subaccount_endpoint({'subauth_id':'SAZDBMMGQ4NDNKOGQ1YZ', 
                                    'endpoint_id':'10925283795052',
                                     'username':'changetest'
                                   })
