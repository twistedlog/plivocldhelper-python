import sys
import plivocldhelper


AUTH_ID = 'YOUR_AUTH_ID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'
API_URL = "http://api.plivo.com"



r = plivocldhelper.RestAPI(AUTH_ID, AUTH_TOKEN, url=API_URL)

print r.create_subaccount_endpoint('SAZDBMMGQ4NDNKOGQ1YZ',
                                   username='subtest', 
                                   domain='subdomplivo.com', 
                                   password='sub')
