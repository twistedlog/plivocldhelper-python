import sys
import plivocldhelper


AUTH_ID = 'YOUR_AUTH_ID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'

r = plivocldhelper.RestAPI(AUTH_ID, AUTH_TOKEN)
params = {'answer_url':'http://yoururl.com',
          'app_name':'My App Name'
         }
print r.create_application(params)
