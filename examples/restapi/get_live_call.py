import sys
import plivocldhelper

try:
    calluuid = sys.argv[1]
except IndexError:
    print "need CALLUUID"
    sys.exit(1)


# Sid and AuthToken
AUTH_ID = 'YOUR_AUTH_ID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'
API_URL = "http://api.plivo.com"

r = plivocldhelper.RestAPI(AUTH_ID, AUTH_TOKEN, url=API_URL)
print r.get_live_call(calluuid)
