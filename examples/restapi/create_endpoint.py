import plivocldhelper

AUTH_ID = 'YOUR_AUTH_ID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'

r = plivocldhelper.RestAPI(AUTH_ID, AUTH_TOKEN)
params = {'username':'test', 'domain':'myname.plivo.com', 'password':'test'}
print r.create_endpoint(params)


